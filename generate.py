# -*- coding: utf-8 -*-
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("index.html", "Accueil"),
    ("services.html", "Nos services"),
    ("comment-ca-marche.html", "Comment ça marche"),
    ("paiement.html", "Paiement"),
    ("contact.html", "Contact"),
]

SERVICES = [
    {
        "slug": "cv-lettre",
        "title": "CV & lettre de motivation",
        "short": "Un CV clair et une lettre qui donnent envie de vous recevoir en entretien.",
        "price": "1 000 – 5 000 FCFA",
        "tiers": [
            ("Léger", "CV seul ou lettre seule, 1 page", "1 000 FCFA"),
            ("Standard", "CV + lettre de motivation", "3 000 FCFA"),
            ("Complet", "CV détaillé (2 pages) + lettre + relecture approfondie", "5 000 FCFA"),
        ],
        "hero_desc": "Un CV structuré et une lettre de motivation sur mesure, rédigés pour le poste que vous visez — livrés en PDF et en Word, prêts à envoyer.",
        "fields": [
            ("nom", "text", "Nom complet", True, None, None),
            ("telephone", "tel", "Téléphone / WhatsApp", True, None, None),
            ("email", "email", "Adresse email", True, None, None),
            ("poste_vise", "text", "Poste ou métier visé", True, None, None),
            ("formule", "select", "Formule souhaitée", True, None, ["CV seul", "Lettre de motivation seule", "CV + lettre de motivation"]),
            ("experience", "textarea", "Votre parcours (formations, expériences, compétences)", True, "Listez les points essentiels, même en vrac — nous mettrons en forme.", None),
            ("delai", "select", "Délai souhaité", False, None, ["Standard (le jour même)", "Urgent (moins de 2h)"]),
        ],
    },
    {
        "slug": "business-plan",
        "title": "Business plan simple",
        "short": "Un business plan clair pour présenter votre projet à une banque, une coopérative ou un partenaire.",
        "price": "1 000 – 5 000 FCFA",
        "tiers": [
            ("Léger", "Note de synthèse, 1-2 pages (présentation + chiffres clés)", "1 000 FCFA"),
            ("Standard", "Business plan complet, 4-6 pages (projet, marché, prévisionnel simplifié)", "3 000 FCFA"),
            ("Complet", "Business plan détaillé, 8-10 pages avec prévisionnel sur 3 ans", "5 000 FCFA"),
        ],
        "hero_desc": "Un document structuré (présentation du projet, marché, prévisionnel financier simplifié) pour appuyer une demande de financement ou clarifier votre projet.",
        "fields": [
            ("nom", "text", "Nom complet", True, None, None),
            ("telephone", "tel", "Téléphone / WhatsApp", True, None, None),
            ("email", "email", "Adresse email", True, None, None),
            ("nom_projet", "text", "Nom du projet / de l'activité", True, None, None),
            ("secteur", "text", "Secteur d'activité", True, None, None),
            ("description_activite", "textarea", "Décrivez votre activité et votre objectif", True, "Que vendez-vous, à qui, et pourquoi ce projet ?", None),
            ("budget_estime", "text", "Budget de démarrage estimé (FCFA)", False, None, None),
            ("objectif", "select", "Ce document servira surtout à", True, None, ["Demande de financement bancaire", "Dossier coopérative / microfinance", "Usage personnel / clarifier le projet", "Autre"]),
        ],
    },
    {
        "slug": "traduction",
        "title": "Traduction de documents",
        "short": "Traduction français ↔ anglais de vos documents administratifs, académiques ou professionnels.",
        "price": "1 000 – 5 000 FCFA",
        "tiers": [
            ("Léger", "1 page", "1 000 FCFA"),
            ("Standard", "3 pages", "3 000 FCFA"),
            ("Complet", "5 pages (au-delà, tarif sur devis)", "5 000 FCFA"),
        ],
        "hero_desc": "Traduction fidèle et bien mise en page de vos documents, du français vers l'anglais ou de l'anglais vers le français.",
        "fields": [
            ("nom", "text", "Nom complet", True, None, None),
            ("telephone", "tel", "Téléphone / WhatsApp", True, None, None),
            ("email", "email", "Adresse email", True, None, None),
            ("sens", "select", "Sens de traduction", True, None, ["Français → Anglais", "Anglais → Français"]),
            ("type_document", "text", "Type de document (diplôme, contrat, lettre, etc.)", True, None, None),
            ("nb_pages", "text", "Nombre de pages estimé", False, None, None),
            ("domaine", "select", "Domaine du document", False, None, ["Général", "Académique", "Juridique / administratif", "Professionnel", "Autre"]),
            ("precisions", "textarea", "Précisions utiles", False, "Délai, mise en page particulière, document à faire suivre par email…", None),
        ],
    },
    {
        "slug": "administratif",
        "title": "Rédaction administrative",
        "short": "Courriers et demandes officielles rédigés dans les formes attendues.",
        "price": "1 000 – 5 000 FCFA",
        "tiers": [
            ("Léger", "Courrier simple, 1 page", "1 000 FCFA"),
            ("Standard", "Courrier avec argumentaire détaillé ou plusieurs pièces à mentionner", "3 000 FCFA"),
            ("Complet", "Dossier administratif complet (plusieurs courriers/pièces liées)", "5 000 FCFA"),
        ],
        "hero_desc": "Courrier de demande, réclamation, attestation ou correspondance officielle, rédigé avec les formules et la présentation attendues par l'administration ou l'entreprise destinataire.",
        "fields": [
            ("nom", "text", "Nom complet", True, None, None),
            ("telephone", "tel", "Téléphone / WhatsApp", True, None, None),
            ("email", "email", "Adresse email", True, None, None),
            ("type_courrier", "select", "Type de courrier", True, None, ["Demande d'emploi / de stage", "Réclamation", "Attestation / certificat", "Demande administrative (mairie, préfecture...)", "Autre"]),
            ("destinataire", "text", "Destinataire du courrier", True, None, None),
            ("objet", "text", "Objet de la demande", True, None, None),
            ("elements", "textarea", "Éléments à inclure dans le courrier", True, "Contexte, informations précises à mentionner, pièces jointes existantes…", None),
        ],
    },
    {
        "slug": "fiches-revision",
        "title": "Fiches de révision & résumés",
        "short": "Des résumés clairs pour réviser efficacement, adaptés à votre niveau.",
        "price": "1 000 – 5 000 FCFA",
        "tiers": [
            ("Léger", "1 fiche ou résumé court", "1 000 FCFA"),
            ("Standard", "3 fiches, ou une fiche détaillée par chapitre", "3 000 FCFA"),
            ("Complet", "Dossier de révision complet, 5 fiches ou plus", "5 000 FCFA"),
        ],
        "hero_desc": "Fiches de révision ou résumés de cours, structurés pour aller à l'essentiel et faciliter la mémorisation avant un examen.",
        "fields": [
            ("nom", "text", "Nom complet", True, None, None),
            ("telephone", "tel", "Téléphone / WhatsApp", True, None, None),
            ("email", "email", "Adresse email", True, None, None),
            ("niveau", "select", "Niveau scolaire", True, None, ["Primaire", "Collège", "Lycée", "Université", "Concours / examen professionnel"]),
            ("matiere", "text", "Matière", True, None, None),
            ("chapitre", "text", "Chapitre ou thème concerné", True, None, None),
            ("format_souhaite", "select", "Format souhaité", False, None, ["Résumé court (1-2 pages)", "Fiche détaillée", "Les deux"]),
            ("support", "textarea", "Support de cours disponible", False, "Décrivez ce que vous avez déjà (notes de cours, manuel, sujet type…)", None),
        ],
    },
    {
        "slug": "reseaux-sociaux",
        "title": "Gestion de pages réseaux sociaux",
        "short": "Calendrier de contenu, textes et visuels simples pour faire vivre vos pages.",
        "price": "1 000 – 5 000 FCFA / mois",
        "tiers": [
            ("Léger", "4 publications/mois (textes uniquement)", "1 000 FCFA/mois"),
            ("Standard", "8 publications/mois (textes + visuels simples)", "3 000 FCFA/mois"),
            ("Complet", "12 publications/mois + calendrier de contenu", "5 000 FCFA/mois"),
        ],
        "hero_desc": "Un calendrier de publications, la rédaction des textes et des visuels simples pour animer régulièrement vos pages, sans avoir à y penser chaque jour.",
        "fields": [
            ("nom", "text", "Nom complet", True, None, None),
            ("telephone", "tel", "Téléphone / WhatsApp", True, None, None),
            ("email", "email", "Adresse email", True, None, None),
            ("entreprise", "text", "Nom de l'entreprise / de la marque", True, None, None),
            ("reseaux", "text", "Réseaux concernés (Facebook, Instagram, WhatsApp...)", True, None, None),
            ("frequence", "select", "Nombre de publications par mois souhaité", False, None, ["4 (1/semaine)", "8 (2/semaine)", "12 ou plus"]),
            ("ton", "text", "Ton souhaité (sérieux, convivial, dynamique...)", False, None, None),
            ("visuels_existants", "select", "Avez-vous déjà des visuels (logo, photos) ?", True, None, ["Oui", "Non"]),
            ("precisions", "textarea", "Précisions sur votre activité et vos objectifs", False, None, None),
        ],
    },
    {
        "slug": "google-business",
        "title": "Fiche Google Business",
        "short": "Votre commerce visible sur Google Maps et la recherche Google.",
        "price": "1 000 – 5 000 FCFA",
        "tiers": [
            ("Léger", "Création et configuration de base (infos, horaires, catégorie)", "1 000 FCFA"),
            ("Standard", "+ ajout de photos et description optimisée", "3 000 FCFA"),
            ("Complet", "Configuration complète + optimisation pour la recherche locale", "5 000 FCFA"),
        ],
        "hero_desc": "Création et configuration complète de votre fiche Google Business (nom, adresse, horaires, catégorie, photos) pour apparaître sur Google Maps et dans les recherches locales.",
        "fields": [
            ("nom", "text", "Nom complet", True, None, None),
            ("telephone", "tel", "Téléphone / WhatsApp", True, None, None),
            ("email", "email", "Adresse email", True, None, None),
            ("nom_commerce", "text", "Nom du commerce", True, None, None),
            ("adresse_commerce", "textarea", "Adresse complète du commerce", True, "Quartier, ville, repère si utile", None),
            ("categorie", "text", "Catégorie d'activité (restaurant, boutique, salon...)", True, None, None),
            ("horaires", "textarea", "Horaires d'ouverture", False, None, None),
            ("site_existant", "text", "Site web ou page existante (optionnel)", False, None, None),
        ],
    },
]

WHATSAPP_NUMBER = "237696477138"
WHATSAPP_DISPLAY = "+237 696 47 71 38"
EMAIL = "claudebell732@gmail.com"


def nav_html(active, prefix=""):
    items = []
    for href, label in NAV:
        cls = ' class="active"' if href == active else ""
        items.append('<li><a href="{p}{h}"{c}>{l}</a></li>'.format(p=prefix, h=href, c=cls, l=label))
    return "\n        ".join(items)


def head(title, description, prefix=""):
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Prestige Services</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>""".format(title=title, desc=description, p=prefix)


def header_nav(active, prefix=""):
    return """<header class="site-header">
  <div class="container">
    <a class="brand" href="{p}index.html"><span class="mark" aria-hidden="true"></span>Prestige Services</a>
    <nav class="main-nav" aria-label="Navigation principale">
      <ul>
        {nav}
      </ul>
    </nav>
    <button class="nav-toggle" aria-label="Ouvrir le menu" aria-expanded="false">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    </button>
  </div>
  <div id="mobile-nav">
    <ul>
      {nav}
    </ul>
  </div>
</header>""".format(nav=nav_html(active, prefix), p=prefix)


def footer(prefix=""):
    return """<footer class="site-footer">
  <div class="container">
    <div>
      <strong style="font-family:var(--serif);font-size:1.1rem;color:#fff;">Prestige Services</strong>
      <p class="small" style="margin-top:8px;max-width:52ch;">Des services administratifs, rédactionnels et numériques réalisés à distance, pensés pour être simples, rapides et fiables.</p>
    </div>
    <ul class="foot-links">
      <li><a href="{p}services.html">Nos services</a></li>
      <li><a href="{p}comment-ca-marche.html">Comment ça marche</a></li>
      <li><a href="{p}paiement.html">Paiement</a></li>
      <li><a href="{p}contact.html">Contact</a></li>
      <li><a href="https://wa.me/{wa}" target="_blank" rel="noopener">WhatsApp</a></li>
    </ul>
    <div class="foot-bottom small">
      <span>© 2026 Prestige Services — Cameroun</span>
      <span>{email}</span>
    </div>
  </div>
</footer>
<a class="whatsapp-fab" href="https://wa.me/{wa}" target="_blank" rel="noopener" aria-label="Contacter sur WhatsApp">
  <svg viewBox="0 0 32 32" fill="currentColor"><path d="M16 3C9.4 3 4 8.4 4 15c0 2.3.6 4.5 1.8 6.4L4 29l7.8-1.8c1.8 1 3.9 1.5 6.2 1.5 6.6 0 12-5.4 12-12S22.6 3 16 3zm0 21.8c-2 0-3.9-.5-5.6-1.5l-.4-.2-4.6 1 1-4.5-.3-.4C4.9 17.4 4.3 15.6 4.3 15.6c0-5.5 4.5-10 10-10s10 4.5 10 10-4.4 9.2-8.3 9.2zm5.5-7.4c-.3-.2-1.8-.9-2-1-.3-.1-.5-.2-.7.2s-.8 1-.9 1.1c-.2.2-.3.2-.6.1-.3-.2-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6.1-.1.3-.3.4-.5.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5 0-.2-.7-1.7-1-2.3-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.4s1 2.8 1.2 3c.1.2 2 3.1 4.9 4.3.7.3 1.2.5 1.6.6.7.2 1.3.2 1.8.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.2-.6-.4z"/></svg>
</a>
<script src="{p}assets/script.js"></script>
</body>
</html>""".format(p=prefix, wa=WHATSAPP_NUMBER, email=EMAIL)


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


# --------------------------------------------------------------------
# INDEX
# --------------------------------------------------------------------
def page_index():
    prefix = ""
    cards = ""
    for s in SERVICES[:6]:
        cards += """
        <a class="card" href="services/{slug}.html">
          <span class="price">{price}</span>
          <h3>{title}</h3>
          <p>{short}</p>
          <span class="go">Voir le service →</span>
        </a>""".format(**s)

    body = """
<main>
  <section class="hero">
    <div class="container">
      <span class="eyebrow">Services à distance · Cameroun</span>
      <h1>Vos documents et démarches, pris en charge du début à la fin.</h1>
      <p class="lead">CV, business plan, traductions, courriers administratifs, fiches de révision, réseaux sociaux, fiche Google Business — commandez en ligne, payez par Mobile Money, recevez votre travail sous 2h.</p>
      <div class="hero-actions">
        <a class="btn btn-gold" href="services.html">Voir les services</a>
        <a class="btn btn-outline" href="comment-ca-marche.html">Comment ça marche</a>
      </div>
      <div class="hero-trust">
        <span><span class="dot"></span>Paiement Mobile Money sécurisé</span>
        <span><span class="dot"></span>Livraison en 2h minimum après paiement</span>
        <span><span class="dot"></span>Commande 100% en ligne, sans déplacement</span>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Simple</span>
        <h2>Pourquoi passer par Prestige Services</h2>
      </div>
      <div class="grid">
        <div class="card">
          <span class="num">01</span>
          <h3>Rapide</h3>
          <p>Un formulaire par service, quelques minutes pour commander. Le travail démarre dès la confirmation du paiement.</p>
        </div>
        <div class="card">
          <span class="num">02</span>
          <h3>Simple</h3>
          <p>Pas de compte à créer, pas d'application à installer. Tout se passe sur le site et sur WhatsApp.</p>
        </div>
        <div class="card">
          <span class="num">03</span>
          <h3>Fiable</h3>
          <p>Un interlocuteur unique, un suivi par WhatsApp et une livraison garantie en 2h minimum après paiement confirmé.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="bg-deep">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Nos services</span>
        <h2>Sept services, un seul interlocuteur</h2>
      </div>
      <div class="grid">{cards}
      </div>
      <div style="margin-top:28px;">
        <a class="btn btn-seal" href="services.html">Voir tous les services et les tarifs</a>
      </div>
    </div>
  </section>

  <section class="bg-ink">
    <div class="container text-center">
      <h2>Une démarche à faire réaliser ?</h2>
      <p class="lead" style="margin:0 auto 22px;max-width:44ch;color:#D8D2C2;">Choisissez votre service, remplissez le formulaire, et suivez votre commande directement sur WhatsApp.</p>
      <a class="btn btn-gold" href="services.html">Commencer une commande</a>
    </div>
  </section>
</main>
""".format(cards=cards)

    write("index.html", head("Accueil", "Services à distance au Cameroun : CV, business plan, traduction, courriers administratifs, fiches de révision, réseaux sociaux, fiche Google Business.", prefix)
          + header_nav("index.html", prefix) + body + footer(prefix))


# --------------------------------------------------------------------
# SERVICES (liste)
# --------------------------------------------------------------------
def page_services():
    prefix = ""
    cards = ""
    for i, s in enumerate(SERVICES):
        cards += """
        <a class="card" href="services/{slug}.html">
          <span class="num">{n:02d}</span>
          <h3>{title}</h3>
          <p>{short}</p>
          <span class="price">{price}</span>
          <span class="go">Commander →</span>
        </a>""".format(n=i + 1, **s)

    body = """
<main>
  <section class="hero" style="padding-bottom:40px;">
    <div class="container">
      <span class="eyebrow">Catalogue</span>
      <h1>Nos services</h1>
      <p class="lead">Sept services réalisés à distance. Choisissez le vôtre pour voir le détail et passer commande — les tarifs sont indicatifs et peuvent varier selon la complexité du travail.</p>
    </div>
  </section>
  <section>
    <div class="container">
      <div class="grid">{cards}
      </div>
    </div>
  </section>
</main>
""".format(cards=cards)

    write("services.html", head("Nos services", "La liste complète des services proposés par Prestige Services avec leurs tarifs indicatifs.", prefix)
          + header_nav("services.html", prefix) + body + footer(prefix))


# --------------------------------------------------------------------
# PAGE PAR SERVICE
# --------------------------------------------------------------------
def field_html(name, ftype, label, required, hint, options):
    req_attr = "required" if required else ""
    req_mark = ' <span class="required-mark">*</span>' if required else ""
    hint_html = '<span class="hint">{}</span>'.format(hint) if hint else ""
    if ftype == "textarea":
        control = '<textarea name="{n}" {r}></textarea>'.format(n=name, r=req_attr)
    elif ftype == "select":
        opts = "".join('<option value="{o}">{o}</option>'.format(o=o) for o in options)
        control = '<select name="{n}" {r}><option value="" disabled selected>Choisir…</option>{opts}</select>'.format(n=name, r=req_attr, opts=opts)
    else:
        control = '<input type="{t}" name="{n}" {r}>'.format(t=ftype, n=name, r=req_attr)
    return """      <div class="field">
        <label>{label}{req}{hint}</label>
        {control}
      </div>""".format(label=label, req=req_mark, hint=hint_html, control=control)


def tiers_html(tiers):
    rows = ""
    for label, desc, price in tiers:
        rows += """
        <div class="pay-row">
          <div>
            <span class="pay-badge">{label}</span>
            <div class="label" style="margin-top:6px;max-width:44ch;">{desc}</div>
          </div>
          <div class="value">{price}</div>
        </div>""".format(label=label, desc=desc, price=price)
    return rows


def page_service(s):
    prefix = "../"
    fields_html = "\n".join(field_html(*f) for f in s["fields"])
    others = [x for x in SERVICES if x["slug"] != s["slug"]][:3]
    others_html = ""
    for o in others:
        others_html += """
        <a class="card" href="{slug}.html">
          <h3>{title}</h3>
          <p>{short}</p>
          <span class="price">{price}</span>
        </a>""".format(**o)

    body = """
<main>
  <section class="svc-hero">
    <div class="container">
      <span class="eyebrow">Service</span>
      <h1>{title}</h1>
      <p>{hero_desc}</p>
      <div class="svc-price"><span class="amount">{price}</span></div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Tarif selon le volume</span>
        <h2>Combien ça coûte</h2>
        <p class="small">Le tarif dépend du volume de travail (nombre de pages, de fiches ou de publications selon le service). Précisez votre besoin dans le formulaire ci-dessous, le tarif exact vous sera confirmé avant paiement.</p>
      </div>
      <div class="receipt" style="margin-bottom:44px;">{tiers}
      </div>
    </div>
  </section>

  <section class="bg-deep">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Étape 1 sur 3</span>
        <h2>Décrivez votre besoin</h2>
        <p class="small">Remplissez ce formulaire, il ouvrira WhatsApp avec un récapitulatif prêt à envoyer. La commande est aussi enregistrée automatiquement pour notre suivi.</p>
      </div>

      <form class="order-form" data-service="{title}">
        {fields}
        <div class="form-status" role="status" aria-live="polite"></div>
        <button class="btn btn-gold btn-block" type="submit">Envoyer ma commande</button>
        <p class="small mt-0">En envoyant ce formulaire, WhatsApp s'ouvre avec le récapitulatif de votre commande. Il ne vous restera qu'à effectuer le paiement et à joindre la preuve — voir <a href="../paiement.html">la page Paiement</a>.</p>
      </form>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Étapes 2 et 3</span>
        <h2>Paiement puis livraison</h2>
      </div>
      <div class="steps">
        <div class="step">
          <span class="n">1</span>
          <h3>Commande</h3>
          <p>Vous remplissez le formulaire ci-dessus.</p>
        </div>
        <div class="step">
          <span class="n">2</span>
          <h3>Paiement</h3>
          <p>Vous envoyez le montant par Mobile Money puis la preuve par WhatsApp.</p>
        </div>
        <div class="step">
          <span class="n">3</span>
          <h3>Réalisation</h3>
          <p>Le travail démarre dès la confirmation du paiement reçu.</p>
        </div>
        <div class="step">
          <span class="n">4</span>
          <h3>Livraison</h3>
          <p>Vous recevez votre document sous 2h minimum, par email ou WhatsApp.</p>
        </div>
      </div>
      <div style="margin-top:24px;">
        <a class="btn btn-seal" href="../paiement.html">Voir les instructions de paiement</a>
      </div>
    </div>
  </section>

  <section class="bg-deep">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Autres services</span>
        <h2>Vous avez peut-être aussi besoin de</h2>
      </div>
      <div class="grid">{others}
      </div>
    </div>
  </section>
</main>
""".format(title=s["title"], hero_desc=s["hero_desc"], price=s["price"], fields=fields_html, others=others_html, tiers=tiers_html(s["tiers"]))

    write("services/{}.html".format(s["slug"]),
          head(s["title"], s["short"], prefix) + header_nav("services.html", prefix) + body + footer(prefix))


# --------------------------------------------------------------------
# COMMENT ÇA MARCHE
# --------------------------------------------------------------------
def page_comment():
    prefix = ""
    body = """
<main>
  <section class="hero" style="padding-bottom:40px;">
    <div class="container">
      <span class="eyebrow">Le processus</span>
      <h1>Comment ça marche</h1>
      <p class="lead">Quatre étapes, du formulaire à la livraison. Le travail ne démarre jamais avant la confirmation du paiement.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="steps">
        <div class="step">
          <span class="n">1</span>
          <h3>Commande</h3>
          <p>Vous choisissez un service, remplissez son formulaire en ligne avec les informations nécessaires au travail.</p>
        </div>
        <div class="step">
          <span class="n">2</span>
          <h3>Paiement</h3>
          <p>Vous envoyez le montant indiqué par Orange Money ou MTN Mobile Money, puis la capture d'écran de paiement par WhatsApp.</p>
        </div>
        <div class="step">
          <span class="n">3</span>
          <h3>Réalisation</h3>
          <p>Dès que le paiement est confirmé, le travail démarre. Aucune réalisation ne commence avant cette confirmation.</p>
        </div>
        <div class="step">
          <span class="n">4</span>
          <h3>Livraison</h3>
          <p>Vous recevez votre document fini par email ou WhatsApp, sous 2 heures minimum après la confirmation du paiement.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="bg-deep">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Bon à savoir</span>
        <h2>Ce que vous pouvez attendre</h2>
      </div>
      <div class="grid">
        <div class="card">
          <h3>Un formulaire par service</h3>
          <p>Chaque service a son propre formulaire, avec uniquement les informations utiles à sa réalisation.</p>
        </div>
        <div class="card">
          <h3>Un suivi par WhatsApp</h3>
          <p>Après l'envoi du formulaire, WhatsApp s'ouvre avec le récapitulatif de votre commande, prêt à être envoyé.</p>
        </div>
        <div class="card">
          <h3>Un délai clair</h3>
          <p>Le délai de livraison est d'au moins 2 heures après la confirmation du paiement, selon la complexité du travail.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="bg-ink text-center">
    <div class="container">
      <h2>Prêt à commander ?</h2>
      <a class="btn btn-gold" href="services.html">Voir les services</a>
    </div>
  </section>
</main>
"""
    write("comment-ca-marche.html", head("Comment ça marche", "Les quatre étapes d'une commande : commande, paiement, réalisation, livraison.", prefix)
          + header_nav("comment-ca-marche.html", prefix) + body + footer(prefix))


# --------------------------------------------------------------------
# PAIEMENT
# --------------------------------------------------------------------
def page_paiement():
    prefix = ""
    body = """
<main>
  <section class="hero" style="padding-bottom:40px;">
    <div class="container">
      <span class="eyebrow">Paiement</span>
      <h1>Payer votre commande</h1>
      <p class="lead">Le paiement se fait par Mobile Money. Le travail démarre uniquement après confirmation de votre paiement.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="steps" style="margin-bottom:40px;">
        <div class="step">
          <span class="n">1</span>
          <h3>Envoyez le montant</h3>
          <p>Utilisez l'un des deux numéros ci-dessous, selon votre opérateur.</p>
        </div>
        <div class="step">
          <span class="n">2</span>
          <h3>Faites une capture</h3>
          <p>Prenez une capture d'écran ou une photo de la confirmation de paiement.</p>
        </div>
        <div class="step">
          <span class="n">3</span>
          <h3>Envoyez-la sur WhatsApp</h3>
          <p>Envoyez la capture au numéro WhatsApp indiqué, avec le nom du service commandé.</p>
        </div>
        <div class="step">
          <span class="n">4</span>
          <h3>Le travail démarre</h3>
          <p>Dès confirmation reçue, votre commande est prise en charge — livraison sous 2h minimum.</p>
        </div>
      </div>

      <div class="receipt">
        <span class="eyebrow">Coordonnées de paiement</span>
        <div class="pay-row">
          <div>
            <div class="label">Orange Money</div>
            <div class="value">696 477 138</div>
          </div>
          <button class="copy-btn" data-copy="696477138">Copier</button>
        </div>
        <div class="pay-row">
          <div>
            <div class="label">MTN Mobile Money</div>
            <div class="value">680 021 646</div>
          </div>
          <button class="copy-btn" data-copy="680021646">Copier</button>
        </div>
        <div class="pay-row">
          <div>
            <div class="label">WhatsApp — preuve de paiement</div>
            <div class="value">+237 696 47 71 38</div>
          </div>
          <a class="btn btn-seal" href="https://wa.me/237696477138" target="_blank" rel="noopener">Ouvrir WhatsApp</a>
        </div>
        <div class="pay-row">
          <div>
            <div class="label">Email de contact</div>
            <div class="value" style="font-size:.92rem;">claudebell732@gmail.com</div>
          </div>
          <button class="copy-btn" data-copy="claudebell732@gmail.com">Copier</button>
        </div>
      </div>
    </div>
  </section>

  <section class="bg-deep">
    <div class="container">
      <div class="grid" style="grid-template-columns:1fr;max-width:760px;">
        <div class="warn-box">
          <strong>Important :</strong> le travail démarre uniquement après confirmation du paiement. Sans preuve de paiement reçue par WhatsApp, la commande reste en attente.
        </div>
        <div class="note-box">
          <strong>Notre engagement :</strong> si le travail livré ne correspond pas à ce qui a été demandé dans le formulaire, nous le corrigeons sans frais supplémentaire. En cas de problème avec votre commande, contactez-nous directement par WhatsApp ou par email — nous répondons rapidement.
        </div>
      </div>
    </div>
  </section>
</main>
"""
    write("paiement.html", head("Paiement", "Instructions de paiement par Orange Money et MTN Mobile Money, et politique de réassurance.", prefix)
          + header_nav("paiement.html", prefix) + body + footer(prefix))


# --------------------------------------------------------------------
# CONTACT
# --------------------------------------------------------------------
def page_contact():
    prefix = ""
    body = """
<main>
  <section class="hero" style="padding-bottom:40px;">
    <div class="container">
      <span class="eyebrow">Contact</span>
      <h1>Nous contacter</h1>
      <p class="lead">Une question avant de commander, ou besoin d'un suivi sur une commande en cours ? Écrivez-nous directement.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="grid" style="grid-template-columns:1fr;max-width:560px;">
        <div class="receipt">
          <div class="pay-row">
            <div>
              <div class="label">WhatsApp</div>
              <div class="value">+237 696 47 71 38</div>
            </div>
            <a class="btn btn-seal" href="https://wa.me/237696477138" target="_blank" rel="noopener">Écrire</a>
          </div>
          <div class="pay-row">
            <div>
              <div class="label">Email</div>
              <div class="value" style="font-size:.92rem;">claudebell732@gmail.com</div>
            </div>
            <a class="btn btn-outline" style="color:var(--ink);border-color:var(--line);" href="mailto:claudebell732@gmail.com">Écrire</a>
          </div>
        </div>
        <p class="small">Pour une commande, préférez le formulaire du service concerné dans <a href="services.html">Nos services</a> — vous recevrez une réponse plus rapide.</p>
      </div>
    </div>
  </section>
</main>
"""
    write("contact.html", head("Contact", "Contactez Prestige Services par WhatsApp ou par email.", prefix)
          + header_nav("contact.html", prefix) + body + footer(prefix))


if __name__ == "__main__":
    page_index()
    page_services()
    for s in SERVICES:
        page_service(s)
    page_comment()
    page_paiement()
    page_contact()
    print("Généré :", len(SERVICES) + 4, "pages service/section +", "index.html")
