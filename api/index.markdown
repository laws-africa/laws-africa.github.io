---
title: Content API
position: 7
lead: A broad collection of African legislation data in machine-readable Akoma Ntoso
  XML. Accurate, comprehensive, uniform, and up-to-date.
navbar_item: api
features:
- title: Legislation in XML, HTML, PDF and ePub
  text: Legislation content in machine-friendly, richly structured [Akoma Ntoso XML](http://www.akomantoso.org/),
    HTML, PDF and ePub formats. Work with entire Acts, or focus only on the chapters
    and sections you need.
- title: Embeddable HTML
  text: Beautifully formatted HTML snippets with CSS styling ready to be added to
    your website or app.
- title: Tables of Contents
  text: Automated Tables of Contents that describe the chapters, parts, sections and
    schedules of legislation without needing to work directly with XML or HTML.
- title: Amendments
  text: Details of the amendments that have been applied to a piece legislation, including
    links and details of the amending work.
- title: Publication and Promulgation
  text: Dates and details of the initial publication, including gazette numbers, often
    with links to the gazette PDFs for reference purposes.
- title: Points in Time
  text: Historical points in time for previous amended versions of legislation, where
    available.
benefits: |-
  * The Laws.Africa commons is continuously updated by the community. This includes the maintenance of existing legislation and the addition of new countries and subject areas.
  * The same data model for all countries makes your work across Africa simpler.
  * [Akoma Ntoso](http://www.akomantoso.org/) is the premier global legislative markup standard. It’s an open, non-proprietary standard managed by [OASIS](https://www.oasis-open.org/).
  * Easy to work with: a simple REST API that provides JSON, XML, HTML, PDF and ePub. For many use cases, there is no need to work with XML directly.
plans:
- title: Non-Commercial and Research
  description: FREE for non-commercial uses.
  details: |-
    * Non-profit, academic research, and education.
    * Creative Commons Attribution-NonCommercial-ShareAlike (CC-BY-NC-SA) licencing.
    * Provide attribution to Laws.Africa.
    * Publish your outputs and research.
- title: Commercial Uses
  description: Permissive licensing for commercial use cases.
  details: |-
    * Full access to Laws.Africa content and data on a per-country basis.
    * Provide attribution to Laws.Africa.
    * Commercial support helps to maintain the commons and supports free access to the law, for everyone.
layout: api/index
---

<p class="lead">The Laws.Africa Content API makes it easy to consume and work with the machine-friendly, structured legislation in the Laws.Africa commons. In addition to legislation content, the API includes content for points in time, amendment information, automated Table of Contents generation, and original publication details.</p>

<a href="/api/detail" class="btn btn-primary">Features, Subscriptions and Pricing</a>

```html
# Fetch Section 9 of Cape Town's Animal by-law
$ curl -H "Authorization: Token <ACCESS_TOKEN>" \
  https://api.laws.africa/v2/akn/za-cpt/act/by-law/2011/animal/eng/main/section/9.html

<section class="akn-section" id="section-9" data-id="section-9">
  <h3>9. The rescue of stray dogs</h3>
  <span class="akn-paragraph" id="section-9.paragraph-0" data-id="section-9.paragraph-0">
    <span class="akn-content">
      <span class="akn-p">A <span class="akn-term" data-refersTo="#term-person" id="trm236" data-id="trm236">person</span> who rescues a stray <span class="akn-term" data-refersTo="#term-dog" id="trm237" data-id="trm237">dog</span> shall report the date and time of the rescue and a description of the <span class="akn-term" data-refersTo="#term-dog" id="trm238" data-id="trm238">dog</span> to the <span class="akn-term" data-refersTo="#term-Council" id="trm239" data-id="trm239">Council</span> within twenty four hours.</span>
    </span>
  </span>
</section>
```
{:.mt-4}
