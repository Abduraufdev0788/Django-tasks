from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def home(requests:HttpRequest):
    context ='''
<!doctype html>
<html lang="uz">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Abdurauf — Portfolio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root{
      --bg:#0f1724; /* dark navy */
      --card:#0b1220;
      --muted:#94a3b8;
      --accent:#7c3aed; /* violet */
      --glass: rgba(255,255,255,0.04);
      --glass-2: rgba(255,255,255,0.02);
      color-scheme: dark;
    }
    *{box-sizing:border-box}
    html,body{height:100%}
    body{
      margin:0;
      font-family:Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
      background:linear-gradient(180deg,var(--bg), #061024 120%);
      color:#e6eef8;
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      line-height:1.4;
      padding:32px;
    }
    .container{max-width:1000px;margin:0 auto}

    /* Header */
    header{
      display:flex;align-items:center;justify-content:space-between;margin-bottom:28px;
    }
    .brand{display:flex;gap:14px;align-items:center}
    .logo{
      width:56px;height:56px;border-radius:12px;background:linear-gradient(135deg,var(--accent),#4f46e5);
      display:flex;align-items:center;justify-content:center;font-weight:800;color:white;font-size:20px;box-shadow:0 6px 18px rgba(0,0,0,0.6);
    }
    nav a{color:var(--muted);text-decoration:none;margin-left:18px}
    nav a:hover{color:#fff}

    /* Hero */
    .hero{display:grid;grid-template-columns:1fr 340px;gap:28px;align-items:center;margin-bottom:26px}
    .intro h1{font-size:28px;margin:0 0 6px}
    .intro p{margin:0;color:var(--muted)}
    .cta{margin-top:18px}
    .btn{
      display:inline-block;padding:10px 14px;border-radius:10px;background:linear-gradient(90deg,var(--accent),#5b21b6);color:white;text-decoration:none;font-weight:600;box-shadow:0 6px 18px rgba(124,58,237,0.18)
    }

    /* Card */
    .card{background:var(--card);border-radius:14px;padding:18px;box-shadow:0 6px 28px rgba(2,6,23,0.6);}

    /* About */
    .about{display:flex;gap:18px;align-items:center}
    .avatar{width:120px;height:120px;border-radius:12px;background-image:linear-gradient(180deg,#0ea5a3,#0284c7);display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:700;color:rgba(255,255,255,0.95)}

    /* Projects */
    .projects-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:14px}
    .project{padding:14px;border-radius:10px;background:linear-gradient(180deg,var(--glass),var(--glass-2));border:1px solid rgba(255,255,255,0.03)}
    .project h3{margin:0 0 8px}
    .tags{display:flex;gap:8px;flex-wrap:wrap}
    .tag{font-size:12px;padding:6px 8px;border-radius:999px;background:rgba(255,255,255,0.03);color:var(--muted)}

    /* Skills */
    .skill{margin-bottom:10px}
    .skill .bar{height:10px;background:rgba(255,255,255,0.06);border-radius:8px;overflow:hidden}
    .skill .level{height:100%;background:linear-gradient(90deg,var(--accent),#4f46e5);display:block}

    /* Contact */
    .contact-form{display:flex;flex-direction:column;gap:8px}
    input,textarea{padding:10px;border-radius:8px;border:1px solid rgba(255,255,255,0.04);background:transparent;color:inherit}
    .muted{color:var(--muted);font-size:13px}

    footer{margin-top:28px;text-align:center;color:var(--muted);font-size:13px}

    /* Responsive */
    @media (max-width:880px){
      .hero{grid-template-columns:1fr;}
      .projects-grid{grid-template-columns:1fr}
      nav a{margin-left:10px}
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="brand">
        <div class="logo">A</div>
        <div>
          <div style="font-weight:700">Jahongir Abdurauf</div>
          <div class="muted" style="font-size:13px">Frontend developer • UI enthusiast</div>
        </div>
      </div>
      <nav>
        <a href="#about">About</a>
        <a href="#projects">Projects</a>
        <a href="#skills">Skills</a>
        <a href="#contact">Contact</a>
      </nav>
    </header>

    <section class="hero">
      <div class="intro card">
        <h1>Salom — men Abdurauf, web ishlab chiqaruvchiman.</h1>
        <p class="muted">Men responsiv saytlar, oddiy interaktivlar va toza front-end kod yozaman. Quyida mening eng yaxshi ishlarim va bog'lanish uchun forma bor.</p>
        <div class="cta">
          <a class="btn" href="#contact">Bog'lanish</a>
        </div>

        <div style="margin-top:18px;display:flex;gap:12px;align-items:center;flex-wrap:wrap">
          <div class="card" style="display:flex;gap:12px;align-items:center;">
            <div style="font-weight:700">5+</div>
            <div class="muted">Tajriba yillari</div>
          </div>
          <div class="card" style="display:flex;gap:12px;align-items:center;">
            <div style="font-weight:700">30+</div>
            <div class="muted">Tugatgan loyihalar</div>
          </div>
        </div>
      </div>

      <aside class="card" style="text-align:center">
        <div class="avatar">N.A</div>
        <h3 style="margin:12px 0 4px">Nasrullayev Abdurauf</h3>
        <div class="muted">Frontend Developer</div>
        <div style="margin-top:12px">
          <div class="muted">Email</div>
          <div style="font-weight:600">Abduraufnasrullayev1210@gmail.com</div>
        </div>
        <div style="margin-top:10px">
          <a class="btn" href="#projects">Portfolio ko'rish</a>
        </div>
      </aside>
    </section>

    <section id="about" class="card" style="margin-bottom:18px">
      <h2 style="margin-top:0">About</h2>
      <div class="about">
        <div style="flex:1">
          <p class="muted">Men HTML, CSS va JavaScript bo'yicha kuchliman. Loyihalarda toza kod, modul tuzilma va responsive dizayn ustida ishlayman. Pastki loyihalar oddiy demo — ularni o'zingiz uchun moslashtirish mumkin.</p>
        </div>
        <div style="width:220px">
          <div class="muted">Qisqacha ma'lumot</div>
          <ul class="muted" style="padding-left:18px;margin:8px 0">
            <li>Frontend: HTML, CSS, JS</li>
            <li>Frameworklar: React (asosiy), Vue (bilaman)</li>
            <li>Tooling: Git, Webpack, Vite</li>
          </ul>
        </div>
      </div>
    </section>

    <section id="projects">
      <h2>Projects</h2>
      <div class="projects-grid">
        <div class="project">
          <h3>SendStore — Cloud storage UI</h3>
          <p class="muted">Responsive front-end for a cloud storage product. Features file list, upload, and user dashboard.</p>
          <div class="tags" style="margin-top:8px">
            <span class="tag">HTML</span>
            <span class="tag">CSS</span>
            <span class="tag">JavaScript</span>
          </div>
        </div>

        <div class="project">
          <h3>Telegram Quiz Bot UI</h3>
          <p class="muted">A simple web interface to manage quiz questions and view results in real-time.</p>
          <div class="tags" style="margin-top:8px">
            <span class="tag">React</span>
            <span class="tag">API</span>
          </div>
        </div>

        <div class="project">
          <h3>Portfolio Template</h3>
          <p class="muted">This template (the one you're viewing) — lightweight, easy to customize, single HTML file.</p>
          <div class="tags" style="margin-top:8px">
            <span class="tag">Template</span>
            <span class="tag">Static</span>
          </div>
        </div>

        <div class="project">
          <h3>Snake Game (Pygame)</h3>
          <p class="muted">A small desktop game built with Python and Pygame — useful for learning and demos.</p>
          <div class="tags" style="margin-top:8px">
            <span class="tag">Python</span>
            <span class="tag">Pygame</span>
          </div>
        </div>
      </div>
    </section>

    <section id="skills" class="card" style="margin-top:18px">
      <h2 style="margin-top:0">Skills</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
        <div>
          <div class="skill">
            <div style="display:flex;justify-content:space-between"><div>HTML & CSS</div><div class="muted">95%</div></div>
            <div class="bar" aria-hidden><span class="level" style="width:95%"></span></div>
          </div>
          <div class="skill">
            <div style="display:flex;justify-content:space-between"><div>JavaScript</div><div class="muted">85%</div></div>
            <div class="bar" aria-hidden><span class="level" style="width:85%"></span></div>
          </div>
        </div>

        <div>
          <div class="skill">
            <div style="display:flex;justify-content:space-between"><div>React</div><div class="muted">80%</div></div>
            <div class="bar" aria-hidden><span class="level" style="width:80%"></span></div>
          </div>
          <div class="skill">
            <div style="display:flex;justify-content:space-between"><div>Git & Tooling</div><div class="muted">75%</div></div>
            <div class="bar" aria-hidden><span class="level" style="width:75%"></span></div>
          </div>
        </div>
      </div>
    </section>

    <section id="contact" style="margin-top:18px">
      <div class="card">
        <h2 style="margin-top:0">Contact</h2>
        <p class="muted">Biror loyiha yoki hamkorlik haqida gaplashsak — yozing.</p>
        <form class="contact-form" onsubmit="handleSubmit(event)">
          <input id="name" placeholder="Ismingiz" required />
          <input id="email" type="email" placeholder="Email" required />
          <textarea id="message" rows="5" placeholder="Xabar" required></textarea>
          <div style="display:flex;gap:10px;align-items:center">
            <button type="submit" class="btn">Yuborish</button>
            <div class="muted">Or send an email: <span style="font-weight:600">Abduraufnasrullayev1210@gmail.com</span></div>
          </div>
        </form>
      </div>
    </section>

    <footer>
      © <span id="year"></span> Abdurauf — Built with ♥
    </footer>
  </div>

  <script>
    document.getElementById('year').innerText = new Date().getFullYear();
    function handleSubmit(e){
      e.preventDefault();
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const message = document.getElementById('message').value;
      // Simple client-side simulation: open default mail client
      const subject = encodeURIComponent('Portfolio contact from ' + name);
      const body = encodeURIComponent(message + '\n\nFrom: ' + name + ' (' + email + ')');
      window.location.href = 'mailto:jahongir@example.com?subject=' + subject + '&body=' + body;
    }
  </script>
</body>
</html>
'''
    return HttpResponse(content=context)

def about(a):
    return HttpResponse("haqida")
def contact(a):
    return HttpResponse("Contcts")

def login(a):
    return HttpResponse("login")

def register(a):
    return HttpResponse("registratsiya")

def profile(a):
    return HttpResponse("Bosh profile")
