const THREE_URL = "https://unpkg.com/three@0.166.1/build/three.module.js";

const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (!prefersReducedMotion) {
  initCryptoScenes();
}

async function initCryptoScenes() {
  const containers = [...document.querySelectorAll("[data-crypto-scene]")];
  if (!containers.length) return;

  let THREE;
  try {
    THREE = await import(THREE_URL);
  } catch {
    document.documentElement.classList.add("three-unavailable");
    return;
  }

  const scenes = containers.map((container) => createScene(THREE, container));

  let running = true;
  document.addEventListener("visibilitychange", () => {
    running = !document.hidden;
  });

  const tick = (time) => {
    if (running) {
      scenes.forEach((scene) => scene.render(time * 0.001));
    }
    requestAnimationFrame(tick);
  };

  requestAnimationFrame(tick);
}

function createScene(THREE, container) {
  const mode = container.dataset.cryptoScene || "orbital-ribbon";
  const renderer = new THREE.WebGLRenderer({
    alpha: true,
    antialias: true,
    preserveDrawingBuffer: true,
  });
  renderer.setClearColor(0x000000, 0);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.6));
  container.appendChild(renderer.domElement);
  container.classList.add("is-ready");

  const scene = new THREE.Scene();
  const camera = new THREE.OrthographicCamera(-3, 3, 3, -3, 0.1, 20);
  camera.position.z = 8;

  const root = new THREE.Group();
  scene.add(root);

  addRibbonPaths(THREE, root, mode);
  addOrbitLines(THREE, root, mode);
  addCipherParticles(THREE, root, mode);

  const resize = () => {
    const width = Math.max(1, container.clientWidth);
    const height = Math.max(1, container.clientHeight);
    const aspect = width / height;
    camera.left = -3 * aspect;
    camera.right = 3 * aspect;
    camera.top = 3;
    camera.bottom = -3;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height, false);
  };

  resize();
  const observer = new ResizeObserver(resize);
  observer.observe(container);

  return {
    render(time) {
      root.rotation.z = Math.sin(time * 0.12) * 0.025;
      root.children.forEach((child, index) => {
        if (child.userData.spin) child.rotation.z += child.userData.spin;
        if (child.userData.float) {
          child.position.y = child.userData.baseY + Math.sin(time * child.userData.float + index) * 0.045;
        }
        if (child.userData.wave) {
          child.scale.x = child.userData.baseScaleX + Math.sin(time * child.userData.wave + index) * 0.015;
        }
      });
      renderer.render(scene, camera);
    },
  };
}

function addRibbonPaths(THREE, root, mode) {
  const configs = {
    "orbital-ribbon": { count: 3, width: 0.032, opacity: 0.2, spread: 0.58 },
    "cipher-nodes": { count: 2, width: 0.022, opacity: 0.14, spread: 0.48 },
    "particle-field": { count: 2, width: 0.018, opacity: 0.12, spread: 0.62 },
    "cipher-ribbon": { count: 3, width: 0.026, opacity: 0.16, spread: 0.54 },
    "secure-core": { count: 2, width: 0.024, opacity: 0.15, spread: 0.46 },
  };
  const config = configs[mode] || configs["orbital-ribbon"];
  const palette = [0xd5b36b, 0xf3ead8, 0x0d1126];

  for (let i = 0; i < config.count; i += 1) {
    const offset = (i - (config.count - 1) / 2) * config.spread;
    const curve = new THREE.CatmullRomCurve3([
      new THREE.Vector3(-2.7, -0.9 + offset * 0.2, 0),
      new THREE.Vector3(-1.55, 1.05 + offset, 0),
      new THREE.Vector3(-0.18, -0.35 - offset * 0.2, 0),
      new THREE.Vector3(1.1, 0.62 - offset * 0.3, 0),
      new THREE.Vector3(2.75, -0.55 + offset * 0.25, 0),
    ]);
    const geometry = new THREE.TubeGeometry(curve, 92, config.width * (i === 1 ? 1.45 : 1), 10, false);
    const material = new THREE.MeshBasicMaterial({
      color: palette[i % palette.length],
      transparent: true,
      opacity: i === 2 ? config.opacity * 0.52 : config.opacity,
      depthWrite: false,
    });
    const ribbon = new THREE.Mesh(geometry, material);
    ribbon.rotation.z = -0.14 + i * 0.08;
    ribbon.userData.float = 0.22 + i * 0.07;
    ribbon.userData.wave = 0.18 + i * 0.04;
    ribbon.userData.baseY = ribbon.position.y;
    ribbon.userData.baseScaleX = ribbon.scale.x;
    root.add(ribbon);
  }
}

function addOrbitLines(THREE, root, mode) {
  const ringColor = mode === "secure-core" ? 0x0d1126 : 0xd5b36b;
  const ringCount = mode === "cipher-ribbon" ? 2 : 3;

  for (let i = 0; i < ringCount; i += 1) {
    const curve = new THREE.EllipseCurve(0, 0, 1.03 + i * 0.45, 0.68 + i * 0.23, 0, Math.PI * 2);
    const points = curve.getPoints(128).map((point) => new THREE.Vector3(point.x, point.y, 0));
    const geometry = new THREE.BufferGeometry().setFromPoints(points);
    const material = new THREE.LineBasicMaterial({
      color: i % 2 ? 0x0d1126 : ringColor,
      transparent: true,
      opacity: i % 2 ? 0.1 : 0.18,
      depthWrite: false,
    });
    const ring = new THREE.LineLoop(geometry, material);
    ring.rotation.z = -0.7 + i * 0.46;
    ring.userData.spin = (i % 2 ? -1 : 1) * (0.00042 + i * 0.00012);
    root.add(ring);
  }
}

function addCipherParticles(THREE, root, mode) {
  const count = mode === "particle-field" ? 90 : 54;
  const radius = mode === "cipher-ribbon" ? 1.65 : 1.85;
  const positions = new Float32Array(count * 3);

  for (let i = 0; i < count; i += 1) {
    const angle = (i / count) * Math.PI * 2;
    const lane = (i % 7) / 7;
    const r = radius * (0.58 + lane * 0.42);
    positions[i * 3] = Math.cos(angle) * r;
    positions[i * 3 + 1] = Math.sin(angle) * r * 0.52;
    positions[i * 3 + 2] = (lane - 0.5) * 0.18;
  }

  const geometry = new THREE.BufferGeometry();
  geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));

  const material = new THREE.PointsMaterial({
    color: mode === "secure-core" ? 0x0d1126 : 0xd5b36b,
    size: mode === "cipher-ribbon" ? 0.018 : 0.026,
    transparent: true,
    opacity: mode === "cipher-ribbon" ? 0.22 : 0.3,
    depthWrite: false,
  });

  const points = new THREE.Points(geometry, material);
  points.userData.spin = mode === "cipher-nodes" ? -0.0008 : 0.0007;
  root.add(points);
}
