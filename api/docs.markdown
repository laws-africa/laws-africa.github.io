---
title: Content API Documentation
lead: Use the Content API to easily fetch legislation in JSON, HTML and XML.
navbar_item: api
layout: api/docs
---

# Quick Start

First, sign up for a free Laws.Africa account at [https://edit.laws.africa/accounts/login/](https://edit.laws.africa/accounts/login/).

Next, get your API token from [https://edit.laws.africa/accounts/profile/api/](https://edit.laws.africa/accounts/profile/api/). In the steps below, you'll need to replace `<YOUR_AUTH_TOKEN>` with your API token.

Let's fetch the details of Cape Town's Animal by-law, in JSON format. This includes the title, publication details and a list of other
API calls you can make for additional details.

```bash
$ curl -H "Authorization: Token <YOUR_AUTH_TOKEN>" \
  https://api.laws.africa/v1/za-cpt/act/by-law/2011/animal.json
```

Laws.Africa can provide us with a Table of Contents for the by-law, also in JSON format. Let's fetch that:

```bash
$ curl -H "Authorization: Token <YOUR_AUTH_TOKEN>" \
  https://api.laws.africa/v1/za-cpt/act/by-law/2011/animal/toc.json
```

Now let's get the HTML content of Section 3 of the by-law, regarding dog registration and licensing:

```bash
$ curl -H "Authorization: Token <YOUR_AUTH_TOKEN>" \
  https://api.laws.africa/v1/za-cpt/act/by-law/2011/animal/eng/main/section/3.html
```

Finally, let's put that HTML into a webpage and include some stylesheets to make it look good:

```html
<link rel="stylesheet" href="//indigo-web.openup.org.za/dist/1.0.1/css/akoma-ntoso.min.css" type="text/css">

<div class="akoma-ntoso">
  <section class="akn-section" id="section-3" data-id="section-3">
    <h3>3. Dog registration and licensing</h3>
    <section class="akn-subsection" id="section-3.1" data-id="section-3.1">
      <span class="akn-num">(1)</span>
      <span class="akn-content"><span class="akn-p">The <span class="akn-term" data-refersTo="#term-owner" id="trm78" data-id="trm78">owner</span> of a property where one or more dogs are kept must register the <span class="akn-term" data-refersTo="#term-dog" id="trm79" data-id="trm79">dog</span> or dogs with the <span class="akn-term" data-refersTo="#term-Council" id="trm80" data-id="trm80">Council</span>.</span></span>
    </section>
    <section class="akn-subsection" id="section-3.2" data-id="section-3.2">
      <span class="akn-num">(2)</span>
      <span class="akn-content"><span class="akn-p">Dog registration must take place within four months of the <span class="akn-term" data-refersTo="#term-dog" id="trm81" data-id="trm81">dog</span>&#8217;s birth or within 30 days of acquiring a <span class="akn-term" data-refersTo="#term-dog" id="trm82" data-id="trm82">dog</span> on property within <span class="akn-term" data-refersTo="#term-Council" id="trm83" data-id="trm83">Council</span>&#8217;s jurisdictional boundaries.</span></span>
    </section>
    <section class="akn-subsection" id="section-3.3" data-id="section-3.3">
      <span class="akn-num">(3)</span>
      <span class="akn-content"><span class="akn-p">The <span class="akn-term" data-refersTo="#term-Council" id="trm84" data-id="trm84">Council</span> may levy a <span class="akn-term" data-refersTo="#term-dog" id="trm85" data-id="trm85">dog</span> license fee in respect of a property where one or more dogs are kept.</span></span>
    </section>
    <section class="akn-subsection" id="section-3.4" data-id="section-3.4">
      <span class="akn-num">(4)</span>
      <span class="akn-content"><span class="akn-p">The amount of the <span class="akn-term" data-refersTo="#term-dog" id="trm86" data-id="trm86">dog</span> license fee may be determined in terms of a resolution of <span class="akn-term" data-refersTo="#term-Council" id="trm87" data-id="trm87">Council</span>. A reduced <span class="akn-term" data-refersTo="#term-dog" id="trm88" data-id="trm88">dog</span> license fee may apply for sterilized dogs.</span></span>
    </section>
  </section>
</div>
```

<div class="card mb-3">
  <div class="card-body">
    <link rel="stylesheet" type="text/css" href="//indigo-web.openup.org.za/dist/1.0.1/css/akoma-ntoso.min.css">

    <div class="akoma-ntoso">
      <section class="akn-section" id="section-3" data-id="section-3">
        <h3>3. Dog registration and licensing</h3>
        <section class="akn-subsection" id="section-3.1" data-id="section-3.1">
          <span class="akn-num">(1)</span>
          <span class="akn-content"><span class="akn-p">The <span class="akn-term" data-refersTo="#term-owner" id="trm78" data-id="trm78">owner</span> of a property where one or more dogs are kept must register the <span class="akn-term" data-refersTo="#term-dog" id="trm79" data-id="trm79">dog</span> or dogs with the <span class="akn-term" data-refersTo="#term-Council" id="trm80" data-id="trm80">Council</span>.</span></span>
        </section>
        <section class="akn-subsection" id="section-3.2" data-id="section-3.2">
          <span class="akn-num">(2)</span>
          <span class="akn-content"><span class="akn-p">Dog registration must take place within four months of the <span class="akn-term" data-refersTo="#term-dog" id="trm81" data-id="trm81">dog</span>&#8217;s birth or within 30 days of acquiring a <span class="akn-term" data-refersTo="#term-dog" id="trm82" data-id="trm82">dog</span> on property within <span class="akn-term" data-refersTo="#term-Council" id="trm83" data-id="trm83">Council</span>&#8217;s jurisdictional boundaries.</span></span>
        </section>
        <section class="akn-subsection" id="section-3.3" data-id="section-3.3">
          <span class="akn-num">(3)</span>
          <span class="akn-content"><span class="akn-p">The <span class="akn-term" data-refersTo="#term-Council" id="trm84" data-id="trm84">Council</span> may levy a <span class="akn-term" data-refersTo="#term-dog" id="trm85" data-id="trm85">dog</span> license fee in respect of a property where one or more dogs are kept.</span></span>
        </section>
        <section class="akn-subsection" id="section-3.4" data-id="section-3.4">
          <span class="akn-num">(4)</span>
          <span class="akn-content"><span class="akn-p">The amount of the <span class="akn-term" data-refersTo="#term-dog" id="trm86" data-id="trm86">dog</span> license fee may be determined in terms of a resolution of <span class="akn-term" data-refersTo="#term-Council" id="trm87" data-id="trm87">Council</span>. A reduced <span class="akn-term" data-refersTo="#term-dog" id="trm88" data-id="trm88">dog</span> license fee may apply for sterilized dogs.</span></span>
        </section>
      </section>
    </div>
  </div>
</div>

# Next steps

See the [Indigo API documentation](https://indigo.readthedocs.io/en/latest/) for full details of working with the Laws.Africa Content API.
