#!/usr/bin/env python3
"""FAME CRYPT — statik sayfa üreticisi.

Ortak header/footer'ı tek kaynaktan (DRY) üretip her sayfanın gövdesiyle
birleştirir. index.html ve kurumsal.html elle yazıldığı için burada
yalnızca alt sayfalar üretilir. Çalıştır: python3 scripts/build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NAV = [
    ("index.html", "Anasayfa"),
    ("kurumsal.html", "Kurumsal"),
    ("urunler.html", "Ürünlerimiz"),
    ("projeler.html", "Projelerimiz"),
    ("akademi.html", "Fame Akademi"),
    ("iletisim.html", "İletişim"),
]


def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="tr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
    <meta name="description" content="{desc}" />
    <link rel="icon" href="assets/images/brand/favicon.png" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Oxanium:wght@400;500;600;700;800&family=Rajdhani:wght@400;500;600;700&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="styles/theme.css" />
    <link rel="stylesheet" href="styles/components.css" />
    <link rel="stylesheet" href="styles/pages.css" />
    <script>document.documentElement.classList.add("js");</script>
  </head>
  <body>
    <a class="skip-link" href="#main">İçeriğe geç</a>
"""


def header(active):
    link_items = []
    for href, label in NAV:
        current = ' aria-current="page"' if href == active else ""
        if href == "kurumsal.html":
            link_items.append(f"""            <li class="nav__item nav__item--has-dropdown">
              <a class="nav__link nav__link--dropdown" href="{href}"{current}>{label}</a>
              <ul class="nav__dropdown" aria-label="Kurumsal bölümler">
                <li><a href="kurumsal.html#hakkimizda">Hakkımızda</a></li>
                <li><a href="kurumsal.html#akademi">Akademik Kadro</a></li>
                <li><a href="kurumsal.html#ortaklar">İş Ortakları</a></li>
                <li><a href="kurumsal.html#sponsorluklar">Etkinlikler</a></li>
              </ul>
            </li>""")
        else:
            link_items.append(f'            <li><a class="nav__link" href="{href}"{current}>{label}</a></li>')
    links = "\n".join(link_items)
    return f"""    <header class="site-header">
      <div class="container">
        <nav class="nav" aria-label="Ana menü">
          <a class="brand" href="index.html" aria-label="FAME CRYPT ana sayfa">
            <img class="brand__mark" src="assets/images/brand/prism-mark.png" alt="" width="40" height="40" />
            <span class="brand__name"><span class="fame">FAME</span><span class="crypt">CRYPT</span></span>
          </a>
          <ul class="nav__menu" id="navMenu">
{links}
          </ul>
          <button class="nav__toggle" aria-label="Menü" aria-expanded="false" aria-controls="navMenu">
            <span></span><span></span><span></span>
          </button>
        </nav>
      </div>
    </header>
"""


FOOTER = """    <footer class="site-footer">
      <div class="container">
        <div class="footer__grid">
          <div class="footer__col">
            <p class="footer__brand-name"><span>FAME</span><span class="crypt">CRYPT</span></p>
            <p class="footer__desc">FAME KRİPTOSİSTEM TASARIM ANALİZ TEST ÜRETİM DANIŞMANLIK İTH. ve İHR. LTD. ŞTİ. ODTÜ Teknokent, Ankara.</p>
            <div class="footer__social">
              <a href="https://tr.linkedin.com/company/famecrypt" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
                <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.8 0 0 .77 0 1.73v20.54C0 23.22.8 24 1.77 24h20.45c.98 0 1.78-.78 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>
              </a>
            </div>
          </div>
          <div class="footer__col"><h4>Kurumsal</h4><ul>
            <li><a href="kurumsal.html">Hakkımızda</a></li>
            <li><a href="kurumsal.html#akademi">Akademik Kadro</a></li>
            <li><a href="kurumsal.html#ortaklar">İş Ortakları</a></li>
            <li><a href="kurumsal.html#sponsorluklar">Sponsorluklar</a></li>
          </ul></div>
          <div class="footer__col"><h4>Çözümler</h4><ul>
            <li><a href="urunler.html">Ürünlerimiz</a></li>
            <li><a href="projeler.html">Projelerimiz</a></li>
            <li><a href="akademi.html">Fame Akademi</a></li>
          </ul></div>
          <div class="footer__col"><h4>İletişim</h4><ul>
            <li><a href="mailto:info@famecrypt.com.tr">info@famecrypt.com.tr</a></li>
            <li><a href="tel:+905389733383">+90 (538) 973 33 83</a></li>
            <li><a href="iletisim.html">İletişim Sayfası</a></li>
          </ul></div>
        </div>
        <div class="footer__bottom">
          <span>© 2017 FAME CRYPT. Tüm hakları saklıdır.</span>
          <span>ODTÜ Teknokent · Çankaya / Ankara</span>
        </div>
      </div>
    </footer>

    <script src="scripts/main.js"></script>
  </body>
</html>
"""


def page(filename, title, desc, active, body):
    html = head(title, desc) + header(active) + body + FOOTER
    (ROOT / filename).write_text(html, encoding="utf-8")
    print("yazıldı:", filename)


# --------------------------------------------------------------------------
# Ürün detay şablonu
# --------------------------------------------------------------------------
def product_detail(filename, eyebrow, title_main, title_accent, lead, paras, features, meta):
    feat = "\n".join(f"            <li>{f}</li>" for f in features)
    para = "\n".join(f'            <p class="product-detail__text">{p}</p>' for p in paras)
    metarows = "\n".join(
        f"            <div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in meta
    )
    return f"""    <main id="main">
      <section class="product-detail-hero">
        <div class="container">
          <a class="back-link" href="urunler.html">← Tüm Ürünler</a>
          <div class="product-detail__layout">
            <div class="reveal">
              <p class="eyebrow">{eyebrow}</p>
              <h1 class="product-detail__title">{title_main} <span class="gradient-text">{title_accent}</span></h1>
              <p class="product-detail__text" style="font-size:1.1rem">{lead}</p>
{para}
              <ul class="feature-list">
{feat}
              </ul>
              <a class="btn btn--primary" href="iletisim.html">İletişime Geç →</a>
            </div>
            <aside class="product-aside reveal">
              <h3>Künye</h3>
              <dl>
{metarows}
              </dl>
            </aside>
          </div>
        </div>
      </section>
    </main>
"""


# --------------------------------------------------------------------------
# 1) TORCUS
# --------------------------------------------------------------------------
page(
    "torcus.html",
    "Torcus — FAME CRYPT",
    "Torcus: SPK, BDDK ve KVKK gereksinimleriyle uyumlu, MPC tabanlı yerli kurumsal cüzdan altyapısı.",
    "urunler.html",
    product_detail(
        "torcus.html", "TORCUS", "MPC Uyumlu", "Kurumsal Cüzdan",
        "Dijital varlık saklama, çoklu onay akışı ve kurumsal operasyon güvenliğini tek mimaride birleştiren yerli cüzdan altyapısı.",
        [
            "<strong>Torcus</strong>, kurumların dijital varlıklarını yüksek güvenlikli, çok taraflı hesaplama (MPC) prensipleriyle saklamasını sağlar. Anahtarlar tek bir noktada bulunmaz; yetki ve onay süreçleri kurum içi rollere göre dağıtılır.",
            "Tasarım yaklaşımı SPK, BDDK ve KVKK gereksinimlerini gözeterek geliştirilir; her işlem izlenebilir, onaylanabilir ve denetlenebilir.",
        ],
        [
            "SPK, BDDK ve KVKK gereksinimleriyle uyumlu tasarım yaklaşımı",
            "Yetkilendirme, işlem onayı ve kurum içi rol ayrımı",
            "Yüksek güvenlikli anahtar yönetimi ve izolasyon prensipleri",
            "MPC tabanlı, tek nokta hatasına dayanıklı mimari",
        ],
        [("Kategori", "Kurumsal Cüzdan"), ("Teknoloji", "MPC · Eşik İmza"),
         ("Uyumluluk", "SPK · BDDK · KVKK"), ("Durum", "AR-GE / Pilot")],
    ),
)

# --------------------------------------------------------------------------
# 2) FAME-VOTE
# --------------------------------------------------------------------------
page(
    "fame-vote.html",
    "Fame-Vote — FAME CRYPT",
    "Fame-Vote: anonimlik, şifreli sayım ve bağımsız doğrulanabilirlik sunan yerli güvenli e-oylama platformu.",
    "urunler.html",
    product_detail(
        "fame-vote.html", "FAME-VOTE", "Güvenli", "E-Oylama Platformu",
        "Oylama süreçlerini internet ortamına taşırken anonimlik, şifreli sayım ve bağımsız doğrulanabilirliği koruyan matematiksel altyapı.",
        [
            "<strong>Fame-Vote</strong>, seçmen gizliliğini bozmadan sonuçların bağımsız biçimde doğrulanabilmesini sağlayan kriptografik protokoller üzerine kuruludur. Oylar şifreli toplanır, anonimlik korunur ve sayım herkesçe denetlenebilir.",
            "Kurum içi seçimlerden oda, birlik ve yüksek katılımlı seçim senaryolarına kadar geniş bir kullanım yelpazesine uyarlanabilir.",
        ],
        [
            "Tam anonimlik ve seçmen gizliliği için kriptografik protokoller",
            "Bağımsız denetlenebilir ve doğrulanabilir sonuç üretimi",
            "Kurum içi, oda, birlik ve yüksek katılımlı seçim senaryoları",
            "Dağıtık güven mimarisi ile merkezi manipülasyona kapalı yapı",
        ],
        [("Kategori", "E-Oylama"), ("Teknoloji", "Homomorfik Şifreleme · ZKP"),
         ("Doğrulama", "Uçtan Uca Denetlenebilir"), ("Durum", "Canlı")],
    ),
)

# --------------------------------------------------------------------------
# 3) DİJİTAL VERİ MÜHENDİSİ
# --------------------------------------------------------------------------
page(
    "dijital-veri.html",
    "Dijital Veri Mühendisi — FAME CRYPT",
    "Dijital Veri Mühendisi: Türkçe için optimize edilmiş, kurum verisiyle güvenli çalışan kurumsal AI asistanı.",
    "urunler.html",
    product_detail(
        "dijital-veri.html", "DİJİTAL VERİ MÜHENDİSİ", "Kurumsal", "AI Asistanı",
        "Türkçe dil anlayışı için iyileştirilmiş, kurum verisiyle güvenli şekilde çalışan ve analiz süreçlerini hızlandıran yapay zeka asistanı.",
        [
            "<strong>Dijital Veri Mühendisi</strong>, kurumların kendi verileriyle güvenli biçimde konuşabildiği; dosya havuzu, veri analizi ve kurumsal bilgi arama deneyimini bir araya getiren bir asistandır.",
            "Kurum içi veri izolasyonu ve kontrollü erişim önceliklidir; veri kurum dışına çıkmadan, gerçek zamanlı kullanım senaryolarına optimize edilmiş bir LLM altyapısıyla çalışır.",
        ],
        [
            "Dosya havuzu, veri analizi ve kurumsal bilgi arama deneyimi",
            "Kurum içi veri güvenliği ve kontrollü erişim yaklaşımı",
            "Gerçek zamanlı kullanım senaryoları için optimize edilmiş LLM altyapısı",
            "Türkçe dil anlayışı için iyileştirilmiş model davranışı",
        ],
        [("Kategori", "Kurumsal AI"), ("Teknoloji", "LLM · RAG"),
         ("Veri", "Kurum İçi İzolasyon"), ("Durum", "AR-GE")],
    ),
)

# --------------------------------------------------------------------------
# 4) PROJELER
# --------------------------------------------------------------------------
PROJECTS = [
    ("01", "KUANTUM SONRASI GÜVENLİK", "Kuantum Ertesi Kriptografi Kütüphanesi",
     ["Yakın gelecekte kuantum bilgisayarlarla yapılacak saldırıların, bugün kullanılan açık anahtarlı kriptosistemleri kullanılamaz hâle getirmesi öngörülüyor. Bu nedenle hem klasik hem de kuantum ataklara dayanıklı sistemlere ihtiyaç duyulacaktır.",
      "Gizliliği uzun süre korunması gereken veriler için güvenli kriptosistemlere geçiş çalışmaları önem kazanmıştır. Bu proje, geleceğe dayanıklı algoritmalara geçişte akademi ile endüstri arasında köprü kurar."], True),
    ("02", "STANDART ALGORİTMALAR", "Kriptografik Kütüphane",
     ["Simetrik ve asimetrik olarak gerekli, standart kabul edilmiş algoritmaların; standartlar ve güvenli gerçekleme teknikleri dikkate alınarak gerçeklenmesini içerir."], False),
    ("03", "ÖZET FONKSİYONLARI", "Hash Fonksiyon Projesi",
     ["Özet fonksiyon algoritmalarının temel yapı taşları, genel kriptanaliz metotları ve güvenlik kriterleri incelenmiş; ardından tasarım ve test çalışmaları yapılmıştır."], False),
    ("04", "AKADEMİ–SANAYİ", "2244 Sanayi Doktora Programı",
     ["Kriptografik kütüphane çalışmaları kapsamında standart algoritmaların güvenli gerçekleme tekniklerine uygun geliştirilmesini ve akademik uzmanlığın sanayi ihtiyaçlarıyla buluşmasını hedefler."], False),
    ("05", "KUANTUM ARAŞTIRMALARI", "Kuantum Bilgisayarlar ve Kriptografi",
     ["Kuantum bilgisayarlarının çalışma prensipleri, kuantum rassal sayı üreteçleri ve kuantum sonrası kriptografi üzerine araştırma ve geliştirme yapılmaktadır."], False),
    ("06", "GÖMÜLÜ SİSTEM GÜVENLİĞİ", "Hafif Sıklet Kriptografi Projesi",
     ["Hafif kriptosistemlerin yapı taşları ve sistem gereksinimleri incelenmiş, tasarım ölçütleri geliştirilmiştir. Literatürdeki hafif blok şifre kriptanaliz yöntemlerini içeren bir kütüphane oluşturulmuştur.",
      "Geliştirilen tasarım ölçütleri çerçevesinde örnek bir blok şifre tasarlanmış ve güvenlik analizleri gerçekleştirilmiştir."], True),
    ("07", "MATEMATİKSEL TASARIM", "Güvenli S-Kutusu Tasarımı",
     ["Literatürdeki ataklara karşı dayanıklılığı kanıtlanmış S-kutularının matematiksel yöntemlerle elde edilmesi ve yazılım yardımıyla sınıflandırılması hedeflenir."], False),
    ("08", "ALGORİTMA TASARIMI", "Güvenli Blok Şifre Tasarımı",
     ["Tüm saldırılara karşı dayanıklı; yeni algoritmalarla birlikte yazılımsal ve donanımsal olarak hızlı gerçeklemelere sahip bir blok şifre algoritması elde edilmesi amaçlanır."], False),
    ("09", "TEST VE DOĞRULAMA", "Rastgele Sayı Üreteci / Testleri",
     ["Kriptografik sistemlerde güvenli rassallık üretimi, test süreçleri ve güvenlik doğrulama yöntemleri üzerine yürütülen çalışmaları kapsar."], False),
    ("10", "DAĞITIK SİSTEMLER", "Blokzincir Tabanlı Sistem Geliştirme",
     ["Blokzincir tabanlı güvenli sistemlerin tasarımı, kriptografik altyapısı ve uygulama senaryoları üzerine geliştirme çalışmalarını içerir."], False),
]


def project_cards():
    out = []
    for idx, eyebrow, title, paras, wide in PROJECTS:
        cls = "project-card project-card--wide" if wide else "project-card"
        p = "\n".join(f"              <p>{x}</p>" for x in paras)
        out.append(f"""            <article class="{cls} reveal">
              <span class="project-card__index">{idx}</span>
              <p class="eyebrow">{eyebrow}</p>
              <h3>{title}</h3>
{p}
            </article>""")
    return "\n".join(out)


page(
    "projeler.html",
    "Projelerimiz — FAME CRYPT",
    "FameCrypt araştırma ve uygulama projeleri: kuantum sonrası kriptografi, hash fonksiyonları, hafif sıklet kriptografi, blok şifre tasarımı ve blokzincir sistemleri.",
    "projeler.html",
    f"""    <main id="main">
      <section class="page-hero">
        <div class="container page-hero__inner reveal">
          <p class="eyebrow">PROJELERİMİZ</p>
          <h1>Araştırmadan<br /><span class="gradient-text">Uygulamaya</span></h1>
          <p class="page-hero__lead">
            Akademik bilgi birikimini artıran araştırma projeleri ile bu birikimi
            ürünlere ve güvenli sistemlere dönüştüren uygulama projelerini birlikte
            yürütüyoruz.
          </p>
        </div>
      </section>

      <section class="section section--tight">
        <div class="container prose-band reveal">
          <p>Firmamız, bir yandan akademik bilgi birikiminin oluşturulması ve artırılması amacıyla araştırma projeleri yürütürken, diğer yandan bu birikimin kullanım alanına aktarılması ve ürün hâline dönüşmesi için uygulama projeleri yürütmektedir.</p>
          <p>Bu projeler; firma öz kaynakları, başta TÜBİTAK olmak üzere çeşitli kurum ve kuruluşların destekleri ve üniversitelerin yakın iş birliğiyle sürdürülmektedir.</p>
        </div>
      </section>

      <section class="section section--tight" aria-labelledby="projects-title">
        <div class="container">
          <div class="section-head reveal">
            <h2 class="section-title" id="projects-title">Proje <span class="accent">Kataloğu</span></h2>
            <p class="section-intro">Kriptografik algoritma tasarımından kuantum sonrası güvenliğe, standart kütüphanelerden blokzincir tabanlı sistemlere.</p>
          </div>
          <div class="projects-grid">
{project_cards()}
          </div>
        </div>
      </section>
    </main>
""",
)

# --------------------------------------------------------------------------
# 5) FAME AKADEMİ — müfredat (örnek tasarımdan birebir, renk uyumlu)
# --------------------------------------------------------------------------
COURSES = [
    ("🛡️", "Siber Güvenlik",
     "Siber güvenliğin temelleri, ağ ve sistem tabanlı saldırı türleri ile savunma mekanizmalarını içeren kapsamlı giriş eğitimi.",
     """<ol class="level-1">
              <li>Siber Güvenliğe Giriş<ol class="level-2"><li>Temel Güvenlik Kavramları</li><li>Katmanlı Güvenlik Yaklaşımı</li><li>Saldırgan Türleri</li><li>Saldırıların Sınıflandırılması</li></ol></li>
              <li>Siber Güvenlik Alanları<ol class="level-2"><li>Kritik Altyapı Güvenliği</li><li>Ağ Güvenliği</li><li>Uygulama Güvenliği</li><li>Bulut Güvenliği</li></ol></li>
              <li>Siber Güvenlik Saldırı Türleri<ol class="level-2"><li>Ağ Tabanlı Saldırılar<ol class="level-3"><li>Enjeksiyon Saldırıları</li><li>DNS Önbellek Zehirlenmesi</li><li>Oturum Ele Geçirme</li><li>Oltalama Saldırıları</li><li>Kaba Kuvvet Saldırıları</li><li>Servis Dışı Bırakma (DoS/DDoS)</li><li>Aradaki Adam Saldırısı</li></ol></li><li>Sistem Tabanlı Saldırılar<ol class="level-3"><li>Virüs</li><li>Solucan</li><li>Truva Atı</li><li>Arka Kapı</li><li>Botlar</li></ol></li></ol></li>
              <li>Siber Tehditlerin Yönetimi<ol class="level-2"><li>Güvenlik Duvarları</li><li>Sanal Özel Ağlar (VPN)</li><li>Güvenlik Kontrol Yönetimi</li><li>Donanım ve Yazılım Önleme</li></ol></li>
            </ol>"""),
    ("🔐", "Kriptografik Protokoller",
     "Kimlik doğrulama, sıfır bilgi ispatları, eşik değerli kriptografi ve çok taraflı hesaplama protokollerinin tasarımı ve analizi.",
     """<ol class="level-1">
              <li>Kriptografik Protokol Temelleri</li>
              <li>Anahtar Değişim Protokolleri</li>
              <li>Taahhüt Şemaları</li>
              <li>Kimlik Doğrulama Protokolleri</li>
              <li>Sıfır Bilgi İspat Protokolleri</li>
              <li>Eşik Değerli Kriptografi<ol class="level-2"><li>Gizli Paylaşım Şemaları</li><li>Doğrulanabilir Gizli Paylaşım</li><li>Eşik Değerli Kriptosistemler</li></ol></li>
              <li>Güvenli Çok Taraflı Hesaplama<ol class="level-2"><li>Eşik Değerli Homomorfik Kriptosistemler</li><li>Oblivious Transfer Protokolleri</li></ol></li>
              <li>Dijital İmza Protokolleri<ol class="level-2"><li>İnkâr Edilemez İmzalar</li><li>Proxy İmzalamalar</li><li>Grup İmzalamalar</li><li>Kör İmzalama Protokolleri</li></ol></li>
            </ol>"""),
    ("💻", "Güvenli Yazılım",
     "Yazılım geliştirme yaşam döngüsünde güvenlik prensipleri, tehdit modelleme ve uygulama seviyesinde modern koruma yöntemleri.",
     """<ol class="level-1">
              <li>Güvenli Yazılım Geliştirme<ol class="level-2"><li>Yazılım Geliştirme Yaşam Döngüsü</li><li>Güvenli Yazılım Nitelikleri</li><li>Tehdit Modelleri</li></ol></li>
              <li>Güvenlik Açıklıkları<ol class="level-2"><li>Kasıtlı Olmayan Açıklıklar</li><li>Kötü Niyetli Açıklıklar</li><li>Karşı Önlemler</li></ol></li>
              <li>Veri Tabanı Güvenliği</li>
              <li>İşletim Sistemleri Güvenliği</li>
              <li>Ağ Güvenliği</li>
              <li>Uygulama Güvenliği</li>
            </ol>"""),
    ("⛓️", "Blokzincir",
     "Blokzincir teknolojisinin çalışma prensipleri, kriptografik temelleri, Bitcoin ekosistemi ve gelecekteki kullanım alanları.",
     """<ol class="level-1">
              <li>Blokzincire Giriş<ol class="level-2"><li>Çalışma Prensibi</li><li>Blok Yapısı</li><li>Blokzincir Gelişimi</li><li>Sistemlerin Sınıflandırması</li></ol></li>
              <li>Kriptografik Temeller<ol class="level-2"><li>Eliptik Eğriler</li><li>Özet Fonksiyonları</li><li>Dijital İmzalamalar</li><li>Sıfır Bilgi İspatları</li><li>Taahhüt Şemaları</li><li>Uzlaşma Protokolleri</li></ol></li>
              <li>Bitcoin Sistemi<ol class="level-2"><li>Bitcoin'e Giriş</li><li>Bitcoin Transferleri</li></ol></li>
              <li>Kısıtlamalar ve Alternatifler<ol class="level-2"><li>Enerji Tüketimi</li><li>Ölçeklenebilirlik</li><li>Mahremiyet</li></ol></li>
              <li>Kullanım Alanları ve Gelecek<ol class="level-2"><li>Dijital Para Birimi</li><li>Akıllı Sözleşmeler</li><li>Bilgi Güvenliği</li><li>Kayıt Saklama</li></ol></li>
            </ol>"""),
    ("📡", "Yan Kanal Analizi",
     "Güç tüketimi, elektromanyetik emisyon, zamanlama sızıntıları ve aktif hata enjeksiyonları üzerinden donanımsal kriptografik zafiyet analizi.",
     """<ol class="level-1">
              <li>Yan Kanal Analizine Giriş<ol class="level-2"><li>Sızıntıların Kaynağı</li><li>Erişim Düzeyine Göre Saldırılar<ol class="level-3"><li>Yerel Saldırılar</li><li>Yakınlık Saldırıları</li><li>Uzaktan Saldırılar</li></ol></li></ol></li>
              <li>Saldırı Çeşitleri<ol class="level-2"><li>Aktif Saldırılar<ol class="level-3"><li>Hata Enjeksiyon Saldırıları</li></ol></li><li>Pasif Saldırılar<ol class="level-3"><li>Zamanlama Saldırıları</li><li>Elektromanyetik Saldırılar</li><li>Akustik Saldırılar</li><li>Güç Analizi Saldırıları</li></ol></li></ol></li>
              <li>Güç Analizi Saldırıları<ol class="level-2"><li>Basit Güç Analizi (SPA)</li><li>Diferansiyel Güç Analizi (DPA)</li><li>Korelasyon Güç Analizi (CPA)</li></ol></li>
            </ol>"""),
    ("🔑", "Temel Kriptografi",
     "Şifreleme biliminin temelleri, klasik algoritmalar, simetrik/asimetrik şifreleme ve modern kriptografik ilkelere derinlemesine bakış.",
     """<ol class="level-1">
              <li>Kriptografiye Giriş ve Temel Kavramlar</li>
              <li>Kriptografinin Amaçları</li>
              <li>Klasik Şifreleme Sistemleri</li>
              <li>Temel Saldırı Türleri<ol class="level-2"><li>Kaba Kuvvet Saldırısı</li><li>Frekans Analizi</li><li>Konfüzyon ve Difüzyon</li></ol></li>
              <li>Kriptoloji İçin Matematik<ol class="level-2"><li>Sayılar Teorisi</li><li>Soyut Cebir</li><li>Boole Fonksiyonlar</li></ol></li>
              <li>Simetrik Şifreler<ol class="level-2"><li>Blok Şifreler (AES, DES)</li><li>Akan Şifreler (LFSR)</li></ol></li>
              <li>Açık Anahtarlı Şifreler<ol class="level-2"><li>Zor Matematik Problemleri</li><li>RSA, Diffie-Hellman, ElGamal</li><li>Eliptik Eğri Kriptografisi</li></ol></li>
              <li>Dijital İmzalar, MAC ve Özet Fonksiyonlar</li>
            </ol>"""),
]


def edu_cards():
    out = []
    for i, (icon, title, summary, content) in enumerate(COURSES):
        out.append(f"""            <article class="edu-card reveal">
              <button class="edu-card__header" aria-expanded="false">
                <span class="edu-card__icon" aria-hidden="true">{icon}</span>
                <span class="edu-card__head-text">
                  <span class="edu-card__title">{title}</span>
                  <span class="edu-card__summary">{summary}</span>
                </span>
                <svg class="edu-card__chevron" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
              </button>
              <div class="edu-card__body"><div class="edu-card__body-inner"><div class="edu-card__content">
                {content}
                <div class="edu-card__contact">
                  <p>Bu eğitim hakkında detaylı bilgi ve kurumunuza özel program için bizimle iletişime geçin.</p>
                  <a class="btn btn--primary" href="mailto:info@famecrypt.com.tr?subject={title} Eğitimi">Bizimle İletişime Geçin →</a>
                </div>
              </div></div></div>
            </article>""")
    return "\n".join(out)


page(
    "akademi.html",
    "Fame Akademi — FAME CRYPT",
    "Fame Akademi; kriptografi, güvenli yazılım, blokzincir, yan kanal analizi ve siber güvenlik alanlarında kurumlara özel eğitim programları sunar.",
    "akademi.html",
    f"""    <main id="main">
      <section class="page-hero">
        <div class="container page-hero__inner reveal">
          <p class="eyebrow">FAME AKADEMİ</p>
          <h1>Eğitim Programları ve<br /><span class="gradient-text">Akademik Yetkinlikler</span></h1>
          <p class="page-hero__lead">
            Kriptografi ve siber güvenlik başta olmak üzere ileri güvenlik teknolojilerinde;
            sağlam teorik temellere dayanan, uygulamaya odaklı ve kurumsal senaryolara
            uyarlanabilir eğitim programları geliştiriyoruz. Detay için bir başlığa tıklayın.
          </p>
        </div>
      </section>

      <section class="section section--tight">
        <div class="container">
          <div class="curriculum-grid">
{edu_cards()}
          </div>
        </div>
      </section>
    </main>
""",
)

# --------------------------------------------------------------------------
# 6) İLETİŞİM
# --------------------------------------------------------------------------
MAP_SRC = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3061.026137682226!2d32.78318041537989!3d39.89606827942918!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14d345f8e5f22eb7%3A0x7d87bc7d2b2c95e1!2sODT%C3%9C%20Teknokent!5e0!3m2!1str!2str!4v1655000000000!5m2!1str!2str"

page(
    "iletisim.html",
    "İletişim — FAME CRYPT",
    "FameCrypt iletişim: ODTÜ Teknokent adresi, e-posta, telefon ve harita. CV'nizi de bize iletebilirsiniz.",
    "iletisim.html",
    f"""    <main id="main">
      <section class="page-hero">
        <div class="container page-hero__inner reveal">
          <p class="eyebrow">İLETİŞİM</p>
          <h1>Bize <span class="gradient-text">Ulaşın</span></h1>
          <p class="page-hero__lead">
            Kriptografi, güvenli yazılım, yapay zeka güvenliği ve kurumsal teknoloji
            ihtiyaçlarınız için ekibimizle doğrudan iletişime geçebilirsiniz.
          </p>
        </div>
      </section>

      <section class="section section--tight">
        <div class="container">
          <div class="contact-grid">
            <div class="contact-info reveal">
              <div class="info-item">
                <span class="info-item__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z"/></svg></span>
                <div><h4>Adres</h4><p>Üniversiteler Mah. İhsan Doğramacı Bulv. Gümüş Bloklar No: 29 Ofis: K1-6, ODTÜ Teknokent, Çankaya / Ankara</p></div>
              </div>
              <a class="info-item" href="mailto:info@famecrypt.com.tr">
                <span class="info-item__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z"/></svg></span>
                <div><h4>E-posta</h4><p>info@famecrypt.com.tr</p></div>
              </a>
              <a class="info-item" href="tel:+905389733383">
                <span class="info-item__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg></span>
                <div><h4>Telefon</h4><p>+90 (538) 973 33 83</p></div>
              </a>
              <a class="info-item" href="https://maps.google.com/?q=ODTÜ+Teknokent" target="_blank" rel="noopener noreferrer">
                <span class="info-item__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5z"/></svg></span>
                <div><h4>Konum</h4><p>Haritada görüntüle → Google Maps</p></div>
              </a>
            </div>
            <div class="contact-map reveal">
              <iframe src="{MAP_SRC}" title="FAME CRYPT konumu — ODTÜ Teknokent" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
            </div>
          </div>

          <!-- CV kutusu -->
          <div class="cv-box reveal">
            <div>
              <p class="eyebrow">KARİYER</p>
              <h3>CV'nizi Bize İletin</h3>
              <p>Kriptografi, yazılım geliştirme ve AR-GE alanlarında yetenekli profesyoneller arıyoruz. CV'nizi aşağıdan yükleyin; dosyanızı seçtikten sonra e-posta uygulamanız üzerinden bize iletebilirsiniz.</p>
            </div>
            <form class="cv-form" action="mailto:info@famecrypt.com.tr" method="post" enctype="multipart/form-data">
              <label class="cv-dropzone" tabindex="0" role="button" aria-label="CV dosyası seç">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 16V4m0 0 4 4m-4-4-4 4"/><path d="M4 16v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-2"/></svg>
                <strong data-cv-label>CV Dosyası Seç</strong>
                <span>PDF, DOC · sürükle-bırak destekli</span>
                <input id="cvInput" name="cv" type="file" accept=".pdf,.doc,.docx" hidden />
              </label>
            </form>
          </div>
        </div>
      </section>
    </main>
""",
)

print("Tamamlandı.")
