---
title: AKN4Africa Recommendation
date: 2021-06-18 11:32:00 +02:00
header_class: bg-lawsafrica-pale-red
navbar_item: publications
lead: Recommendations for using Akoma Ntoso with African legal materials.
---

# Introduction

The Akoma Ntoso (AKN) Naming Convention for uniquely naming documents and elements within them provides a framework for naming documents in a consistent and replicable way. This is crucial for referring to other pieces of legislation (or any of their provisions) from a given AKN document.

The aim of the AKN4Africa Recommendation is to provide guidance on the implementation of this framework in the African context, taking into account documents from African countries and regional bodies and their drafting traditions. The AKN4UN and AKN4EU projects provide similar guidance for applying AKN naming conventions to UN and EU documents.

This Recommendation is meant for users already familiar with the AKN standard and conventions, as the intention is to add to the existing standard rather than reinventing any of it.

Laws.Africa is not an official body like the UN or the EU, but we also haven’t found an existing convention for using AKN in the African context. We are therefore publishing our interpretation of the AKN standard for documents from African jurisdictions:

* based on our experience supporting African governments that are building their own AKN collections, and applying AKN to documents across a number of African jurisdictions;
* as a recommendation to other users of AKN across Africa for how to generate FRBR URIs (and eIds); and
* to help anyone resolving links to Laws.Africa-generated AKN documents.

# Resources

The following resources informed the structure of this document and the issues discussed.

* Akoma Ntoso Naming Convention: [http://docs.oasis-open.org/legaldocml/akn-nc/v1.0/akn-nc-v1.0.html](http://docs.oasis-open.org/legaldocml/akn-nc/v1.0/akn-nc-v1.0.html)
* AKN4UN: [https://unsceb-hlcm.github.io/](https://unsceb-hlcm.github.io/)
* AKN4EU: [https://op.europa.eu/en/web/eu-vocabularies/akn4eu](https://op.europa.eu/en/web/eu-vocabularies/akn4eu)

# Generating FRBR URIs

AKN FRBR URIs are constructed as follows, with the <span style="color:#808080">grey</span> text indicating that an element is optional:

/akn/`2-letter country code`<code><span style="color:#808080">-locality code</span></code>/`doctype`/<code><span style="color:#808080">subtype</span></code>/<code><span style="color:#808080">author</span></code>/`year`/`number`

In general, lowercase all letters and don’t use any spaces.
The sections below go into detail about each of the FRBR URI elements. Before that, we outline our guiding principles when deciding how to structure FRBR URIs in a given jurisdiction.
At the end are example FRBR URIs for regional and country legislation. We have aimed to include an example for each doctype and subtype.

## Guiding principles

### Uniqueness, consistency and replicability

FRBR URIs are used to identify specific documents, or ‘works’ in AKN and FRBR nomenclature. Uniqueness is thus critical.

Consistency and replicability are crucial for accurately referencing (and dereferencing) documents.

When determining the various FRBR URI elements, use the most authoritative source to ensure replicability without coordination. For instance, use Parliament’s numbering system to identify Acts.

### Respecting local traditions

We recommend striking a balance between consistency and local traditions, because a convention should make sense to the people using it. Where it is possible and meaningful to consistently incorporate a jurisdiction’s local naming convention into the FRBR URI, do so.

For example:

* The reference numbers of ACHPR Resolutions have the form ‘ACHPR/Res. 343(LVIII) 2016’. In AKN nomenclature this includes the author (`achpr`), the type (`resolution`), the number (`343`) and the year (`2016`). However, it also includes the session number, `58` (or LVIII). While it isn’t strictly necessary to include the number under the AKN Naming Convention, we include it in the FRBR URIs because it is commonly used when referring to ACHPR Resolutions: <code>/akn/aa/statement/resolution/achpr/2016/<b>58-</b>343</code>.
* ECOWAS documents are referred to as e.g. ‘A/SA.1/12/14’. The subtype (`supplementary-act`), year (`2014`) and number (`1`) are all included, as is the month in which the Supplementary Act was signed. The month isn’t strictly necessary to identify ‘Supplementary Act 1 of 2014’, but because it’s part of the local tradition, we include it in the FRBR URI: <code>/akn/aa-ecowas/act/supplementary-act/2014/<b>12-</b>1</code>.

When including information in FRBR URIs that isn’t strictly necessary, start with more general information and work your way to increasingly specific information (to the right of the FRBR URI) . When we include the session number for ACHPR Resolutions, and the month for ECOWAS documents, they come before the number itself, with a hyphen, because the number is the most specific element.

## Country code

Always use a 2-letter country code, whether the jurisdiction is a literal country or a regional body.

### Literal countries

For countries, use the ISO 3166 2-letter code, e.g. `ke` for Kenya (see [https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2](https://www.google.com/url?q=https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

### Regional bodies

For African Union documents, use `aa` as the country code. We chose this code because there is no official ISO 3166 code for the African Union, the code `au` is already assigned (as are `af` and `ua`), but `aa` is not and can be assigned freely by users.

For other regional bodies in Africa, use `aa` as the country code in combination with a locality code, e.g. `aa-ecowas`.

Note: The non-AU regional bodies in Africa – such as the EAC, ECOWAS, and SADC – are top-level authorities and aren’t sub-places within the AU the way that provinces are within a country. However, we cannot use them as top-level countries because we are constrained by the need for a two-letter country code. We have chosen to place them under the African Union country code (`aa`) rather than another arbitrary country code such as `xx` for ‘Other’.

## Locality code

Locality codes are used for:

* sub-national legislation, e.g. Provincial Acts, County Acts, or Municipal By-laws; and
* regional legislation that uses the `aa` country code.

The locality code is always preceded by a two-letter country code and a hyphen. Hyphens within a locality code are allowed; any spaces or other punctuation should be replaced with hyphens or removed.

Where possible, use the official locality codes assigned by a jurisdiction.

For example,

* Kenyan Counties are assigned numbers from 001 to 047. The FRBR URI for a Mombasa County Act would therefore start `/akn/ke-001/…`.
* In South Africa, municipalities are assigned codes. The FRBR URI for a Municipal By-law in Mbizana would therefore start `/akn/za-ec443/…`.

## Doctype and subtype

For examples of doctypes and subtypes, see the [Example FRBR URIs](#example-frbr-uris) section.

### Doctype

* For legislation – Acts, Regulations, Statutory Instruments, and the like – use `act`. <br>
    These are documents that have the force of law.
* For soft law – Resolutions, Guidelines, Decisions, Model laws, Agreements, and the like – use `statement`. <br>
  These are documents that don’t (or only sometimes) have the force of law, but do still have to do with the law (to varying degrees).
* For case law, use `judgment`.
* For other documents – Policies, Memoranda of Understanding, Yearbooks, Press Releases, and the like – use `doc`. <br>
  This document, for example, would use the `doc` doctype.

### Subtype

* If the document is anything other than an act / statement / judgment / doc, use whatever it calls itself as the subtype, e.g. `act/si` for a Statutory Instrument (‘act’ because it has the force of law).
* The same subtype should always be used with the same doctype: One should be able to reliably predict, for example, that a set of guidelines will always have `statement/guidelines` as the doctype/subtype combination.

#### Regional legislation

Use the full subtype for regional legislation (and not an abbreviated form), because regional legislation applies to multiple jurisdictions and it can’t be assumed that everyone across the region will use the same set of conventional abbreviations.

For document types that typically appear in the plural, e.g. Guidelines, use the plural in the AKN subtype (`guidelines`). If a document type that usually appears in the singular has an instance that appears in the plural, use the singular for that instance. Don’t use both the singular and the plural, or any other variances of a document type, because this lessens the likelihood of documents linking to each other reliably.

If a document type that typically appears in the plural is used in the singular in a given jurisdiction, do use it in the singular in that jurisdiction, but consistently. An example of this is Regulation (`regulation`) in ECOWAS.

#### Country legislation

Use the local tradition for the subtype, because we can assume that people will be familiar with conventional abbreviations within a country. The local tradition will often have an abbreviated form for the subtype, unlike with regional legislation.

Again, don’t use plurals or other variances of document types, as it makes it more difficult for documents to refer to each other reliably and predictably.

Inevitably, a document type will exist for which an abbreviation has already been chosen. When this happens, choose a longer abbreviation for the ‘new’ document type, and leave the existing one as is. For example, Premier’s Notice (`premn`) was added after Provincial Notice (`pn`). Try to map out all subtypes beforehand to avoid such a clash.

Author
------

Include the author to differentiate from the ‘default’ author, and where it’s necessary to clearly differentiate between similar documents with different authors.

For national legislation the author of the work level is not usually specified, as the ‘author’ of national legislation is usually always the same body (e.g. the National Assembly in South Africa).

For example, the default author of African Union legislation is the Assembly of the African Union and is not specified. If a document that is applicable to the African Union was authored by a different body, e.g. the African Commission on Human and Peoples’ Rights, include the author to differentiate it from the default.

Below is a non-exhaustive list of relevant bodies and their ‘author’ codes.

Abbreviate the author only if a body is usually referred to by that abbreviation.

<table class="table table-sm table-bordered">
  <tr>
    <th>Body</th>
    <th>Author code</th>
  </tr>
  <tr>
    <td>African Commission on Human and Peoples’ Rights</td>
    <td><code>achpr</code></td>
  </tr>
  <tr>
    <td>African Union Commission</td>
    <td><code>auc</code></td>
  </tr>
  <tr>
    <td>African Union Specialized Technical Committee on Transport, Transcontinental and Interregional Infrastructure, Energy and Tourism</td>
    <td><code>austc-on-transport-infrastructure-energy-tourism</code></td>
  </tr>
  <tr>
    <td>Committee for the Prevention of Torture in Africa</td>
    <td><code>cpta</code></td>
  </tr>
  <tr>
    <td>Department of Rural Economy and Agriculture of the African Union Commission</td>
    <td><code>auc-department-of-rural-economy-and-agriculture</code></td>
  </tr>
  <tr>
    <td>Organisation of African Unity</td>
    <td><code>oau</code></td>
  </tr>
</table>

Year
----

For the year, use the year of the work, in the format `yyyy`.

In many jurisdictions the Act number and year are formally assigned by Parliament.

The year usually coincides with the year in which it was published, but if an Act was assigned the number / year combination ‘Act 32 of 2019’ but was only published in 2020, use ‘2019’ as the year. This is both to avoid clashes in numbering (in this example there may well also be an ‘Act 32 of 2020’) and to respect the official assignment.

For African Union, EAC, ECOWAS, and SADC documents, use the year of the date of adoption.

## Number

The purpose of the `number` element in the FRBR URI is to clearly identify a given document (in that place, with that subtype, by that author, in that year). It’s the most specific piece of information about a document that can disambiguate it from its peers (e.g. all other Acts in that year).

We use a number whenever available, e.g. an Act number, notice number, Resolution number, etc.

(This is on the assumption that one would never have, for example, two Acts issued in the same year with the same Act number. Where this does happen due to a clerical error, we would add `-b`, `-c`, etc. at the end to the later Act(s), leaving the first Act with that number as is.)

If the number is a Roman numeral, use the Arabic number instead. This goes for the actual number of the document as well as session numbers and the like, if included.

Where there isn’t a number available, for instance the Guidelines on Freedom of Association and Assembly in Africa, use a short phrase, in this case `freedom-of-association-and-assembly`.

Omit:

* the subtype (in this case `guidelines`);
* the author, if applicable; and
* the place (in this case ‘Africa’, already being implied by the `aa` country code – we also omit ‘African Union’ for the same reason),

except when to do so would change the meaning. For example:

* Rules of Procedure of the African Commission on Human and Peoples’ Rights, 2020: 
  <code>/akn/aa/act/<b>rules</b>/achpr/2020/<b>rules-of-</b>procedure</code>
* Statute of the Africa Sports Council: 
  <code>/akn/<b>aa</b>/act/statute/2016/<b>africa-</b>sports-council</code>

When choosing such a phrase it’s important to bear in mind the purpose of the `number` element. If, for example, several ‘progress’ statements are typically issued by a body within a year, you may wish to number them `progress-1`, `progress-2`, etc. for disambiguation. But if each is typically on a different topic, the preference is to number them, for example, `progress-environment`, `progress-public-health`, etc.

### Acts with Chapter numbers

Don’t use a Chapter (or Cap) number when generating an FRBR URI, because they change over time. Use the Act’s number as assigned in the original legislative process.

You can link the Cap number as a piece of document metadata and update it as necessary to ensure references are dereferenced accurately.

### Judgments

Judgment numbers should be derived from an officially assigned Medium Neutral Citation (MNC) if possible. In most cases, the MNC includes a number that is unique either within a year, within a particular court, or both. Use the necessary elements from the MNC to generate a unique FRBR URI.

For example, Kenya Law assigns MNC numbers to Kenyan judgments which include a year and a court code. Judgment 5 of 2019 from the High Court of Kenya would use the FRBR URI <code>/akn/<b>ke</b>/judgment/<b>kehc</b>/<b>2019</b>/<b>5</b></code>. Here, `kehc` identifies the document author: the High Court of Kenya.

## Example FRBR URIs

The tables below aim to include all known document types but will certainly fail, if only because inevitably a new document type will be published in the future. The preceding sections are there to guide users in making the call when the tables fail, and explain how the tables were compiled.

### Regional legislation

* African Union doctypes list compiled from [https://au.int/treaties](https://au.int/treaties) and [https://www.achpr.org/resources](https://www.achpr.org/resources).
* EAC doctypes list compiled from [https://www.eac.int/documents/category/acts-of-the-community](https://www.eac.int/documents/category/acts-of-the-community) and [https://www.eac.int/documents/category/eac-regulations](https://www.eac.int/documents/category/eac-regulations).
* ECOWAS doctypes list compiled from [https://www.ecowas.int/ecowas-law/](https://www.ecowas.int/ecowas-law/).
* SADC doctypes list compiled from [https://www.sadc.int/documents-publications/](https://www.sadc.int/documents-publications/).

#### Documents with the <code>act</code> doctype

<table class="table table-sm table-bordered">
  <tr>
    <th>Document type</th>
    <th>Example</th>
    <th>Subtype</th>
    <th>FRBR URI</th>
  </tr>
  <tr>
    <td>Act</td>
    <td><a href="https://www.eac.int/documents/category/acts-of-the-community">East African Community One Stop Border Posts Act, 2016</a></td>
    <td></td>
    <td><code>/akn/aa-eac/act/2016/one-stop-border-posts</code></td>
  </tr>
  <tr>
    <td rowspan="2">Agreement</td>
    <td><a href="https://au.int/en/treaties/agreement-establishment-african-rehabilitation-institute-ari">Agreement for the Establishment of the African Rehabilitation Institute (ARI)</a></td>
    <td rowspan="2">agreement</td>
    <td><code>/akn/aa/act/agreement/oau/1985/establishment-of-the-african-rehabilitation-institute</code></td>
  </tr>
  <tr>
    <td><a href="https://www.sadc.int/documents-publications/show/6925">Agreement Amending Article 3 of the Protocol on Trade</a></td>
    <td><code>/akn/aa-sadc/act/agreement/2016/amending-article-3-of-the-protocol-on-trade</code></td>
  </tr>
  <tr>
    <td rowspan="4">Charter</td>
    <td><a href="https://au.int/en/treaties/oau-charter-addis-ababa-25-may-1963">OAU Charter</a></td>
    <td rowspan="4">charter</td>
    <td><code>/akn/aa/act/charter/oau/1963/nn</code></td>
  </tr>
  <tr>
    <td><a href="https://au.int/en/treaties/african-youth-charter">African Youth Charter</a></td>
    <td><code>/akn/aa/act/charter/2006/youth</code></td>
  </tr>
  <tr>
    <td><a href="https://www.achpr.org/legalinstruments/detail?id=49">African Charter on Human and Peoples’ Rights</a></td>
    <td><code>/akn/aa/act/charter/achpr/1981/human-and-peoples-rights</code></td>
  </tr>
  <tr>
    <td><a href="https://www.sadc.int/documents-publications/show/836">Charter Establishing the Centre for Coordination of Agricultural Research and Development (CCARDESA)</a></td>
    <td><code>/akn/aa-sadc/act/charter/2010/establishing-the-centre-for-coordination-of-agricultural-research-and-development</code></td>
  </tr>
  <tr>
    <td>Constitution</td>
    <td><a href="https://au.int/en/treaties/constitutive-act-african-union">Constitutive Act of the African Union</a></td>
    <td></td>
    <td><code>/akn/aa/act/2000/constitutive-act</code></td>
  </tr>
  <tr>
    <td>Convention</td>
    <td><a href="https://au.int/en/treaties/general-convention-privileges-and-immunities-organization-african-unity">General Convention on the Privileges and Immunities of the Organization of African Unity</a></td>
    <td>convention</td>
    <td><code>/akn/aa/act/convention/oau/1965/privileges-and-immunities</code></td>
  </tr>
  <tr>
    <td>Directive</td>
    <td><a href="https://www.ecowas.int/ecowas-law/regulations-directives-and-other-acts/70th-ordinary-session-of-council-of-ministers/">Directive C/Dir.1/06/13 on the Organization of the Regional Electricity Market</a></td>
    <td>directive</td>
    <td><code>/akn/aa-ecowas/act/directive/2013/6-1</code></td>
  </tr>
  <tr>
    <td rowspan="2">Pact</td>
    <td><a href="https://au.int/en/treaties/african-union-non-aggression-and-common-defence-pact">The African Union Non-Aggression and Common Defence Pact</a></td>
    <td rowspan="2">pact</td>
    <td><code>/akn/aa/act/pact/2005/non-aggression-and-common-defence</code></td>
  </tr>
  <tr>
    <td><a href="https://www.sadc.int/documents-publications/show/1038">SADC Mutual Defence Pact</a></td>
    <td><code>/akn/aa-sadc/act/pact/2003/mutual-defence</code></td>
  </tr>
  <tr>
    <td rowspan="2">Protocol</td>
    <td><a href="https://www.achpr.org/legalinstruments/detail?id=3">Protocol to the African Charter on Human and Peoples’ Rights on the Rights of Older Persons in Africa</a></td>
    <td rowspan="2">act</td>
    <td rowspan="2">protocol</td>
    <td><code>/akn/aa/act/protocol/2016/achpr-rights-of-older-persons</code></td>
  </tr>
  <tr>
    <td><a href="https://www.sadc.int/documents-publications/show/1933">Protocol on Trade in Services</a></td>
    <td><code>/akn/aa-sadc/act/protocol/2012/trade-in-services</code></td>
  </tr>
  <tr>
    <td>Regulation</td>
    <td><a href="https://www.ecowas.int/ecowas-law/regulations-directives-and-other-acts/73rd-ordinary-session-of-the-council-of-ministers/">Regulation Approving The Work Programme of the ECOWAS Commission, for the 2015 Financial Year</a></td>
    <td>regulation</td>
    <td><code>/akn/aa-ecowas/act/regulation/2014/12-1</code></td>
  </tr>
  <tr>
    <td>Regulations</td>
    <td><a href="https://www.eac.int/documents/category/eac-regulations">East Africa Community Vehicle Load Control (Vehicle Dimensions and Axle Configurations) Regulations, 2018</a></td>
    <td>regulations</td>
    <td><code>/akn/aa-eac/act/regulations/2018/vehicle-load-control-vehicle-dimensions-and-axle-configurations</code></td>
  </tr>
  <tr>
    <td>Rules</td>
    <td><a href="https://www.achpr.org/legalinstruments/detail?id=72">Rules of Procedure of the African Commission on Human and Peoples’ Rights, 2020</a></td>
    <td>rules</td>
    <td><code>/akn/aa/act/rules/achpr/2020/rules-of-procedure</code></td>
  </tr>
  <tr>
    <td>Standard Operating Procedures</td>
    <td><a href="https://www.achpr.org/legalinstruments/detail?id=68">Standard Operating Procedures on the Special Mechanisms of the African Commission on Human and Peoples’ Rights</a></td>
    <td>standard-operating-procedures</td>
    <td><code>/akn/aa/act/standard-operating-procedures/achpr/2020/special-mechanisms</code></td>
  </tr>
  <tr>
    <td>Statute</td>
    <td><a href="https://au.int/en/treaties/statute-africa-sports-council">Statute of the Africa Sports Council</a></td>
    <td>statute</td>
    <td><code>/akn/aa/act/statute/2016/africa-sports-council</code></td>
  </tr>
  <tr>
    <td>Supplementary Act</td>
    <td><a href="https://www.ecowas.int/ecowas-law/find-legislation/46th-ordinary-session-of-the-authority-of-heads-of-state-and-government-abuja-15-december-2014/">Supplementary Act A/SA.1/12/14 on the Improvement of Performance in Higher Education and Scientific Research</a></td>
    <td>supplementary-act</td>
    <td><code>/akn/aa-ecowas/act/supplementary-act/2014/12-1</code></td>
  </tr>
  <tr>
    <td rowspan="2">Treaty</td>
    <td><a href="https://au.int/en/treaties/treaty-establishing-african-economic-community">Treaty Establishing the African Economic Community</a></td>
    <td rowspan="2">treaty</td>
    <td><code>/akn/aa/act/treaty/oau/1991/establishing-the-african-economic-community</code></td>
  </tr>
  <tr>
    <td><a href="https://www.ecowas.int/ecowas-law/treaties/">Economic Community of West African States (ECOWAS) Revised Treaty, 1993</a></td>
    <td><code>/akn/aa-ecowas/act/treaty/1993/ecowas-revised-treaty</code></td>
  </tr>
</table>

#### Documents with the <code>statement</code> doctype

<table class="table table-sm table-bordered">
  <tr>
    <th>Document type</th>
    <th>Example</th>
    <th>Subtype</th>
    <th>FRBR URI</th>
  </tr>
  <tr>
    <td>Comment</td>
    <td><a href="https://www.achpr.org/legalinstruments/detail?id=60">General Comment No. 4 on the African Charter on Human and Peoples’ Rights: The Right to Redress for Victims of Torture and Other Cruel, Inhuman or Degrading Punishment or Treatment (Article 5)</a></td>
    <td>comment</td>
    <td><code>/akn/aa/statement/comment/achpr/2017/4</code></td>
  </tr>
  <tr>
    <td>Decision</td>
    <td><a href="https://www.ecowas.int/ecowas-law/find-legislation/46th-ordinary-session-of-the-authority-of-heads-of-state-and-government-abuja-15-december-2014/">Decision A/Dec.01/12/14 amending Decision A/Dec 2/7/85 Establishing a Travel Certificate for ECOWAS Member States</a></td>
    <td>decision</td>
    <td><code>/akn/aa-ecowas/statement/decision/2014/12-1</code></td>
  </tr>
  <tr>
    <td rowspan="2">Declaration</td>
    <td><a href="https://www.achpr.org/legalinstruments/detail?id=69">Declaration of Principles on Freedom of Expression and Access to Information in Africa, 2019</a></td>
    <td rowspan="2">declaration</td>
    <td><code>/akn/aa/statement/declaration/achpr/2019/principles-on-freedom-of-expression-and-access-to-information</code></td>
  </tr>
  <tr>
    <td><a href="https://www.ecowas.int/ecowas-law/find-legislation/46th-ordinary-session-of-the-authority-of-heads-of-state-and-government-abuja-15-december-2014/">Declaration of the Heads of State and Government of the Economic Community of West African States on the Implementation of the ECOWAS Common External Tariff (CET)</a></td>
    <td><code>/akn/aa-ecowas/statement/declaration/2014/implementation-of-common-external-tariff</code></td>
  </tr>
  <tr>
    <td rowspan="2">Guidelines</td>
    <td><a href="https://www.achpr.org/legalinstruments/detail?id=1">State Reporting Guidelines and Principles* on Articles 21 And 24 of the African Charter relating to Extractive Industries, Human Rights and the Environment</a> <br>
* While the title includes ‘Guidelines and Principles’, the principles inform the guidelines, which are the crux of the document. This will generally be our assumption in a case like this. If in doubt, read the document to see which subtype is more prominent when more than one is given in the title.</td>
    <td rowspan="2">guidelines</td>
    <td><code>/akn/aa/statement/guidelines/achpr/2018/state-reporting-articles-21-and-24</code></td>
  </tr>
  <tr>
    <td><a href="https://www.achpr.org/legalinstruments/detail?id=4">The Guidelines on Combating Sexual Violence and its Consequences in Africa</a></td>
    <td><code>/akn/aa/statement/guidelines/achpr/2017/combating-sexual-violence-and-its-consequences</code></td>
  </tr>
  <tr>
    <td>Questions</td>
    <td><a href="https://www.achpr.org/legalinstruments/detail?id=51">Indicative questions to State Parties in respect of Article 5 of the African Charter</a></td>
    <td>questions</td>
    <td><code>/akn/aa/statement/questions/cpta/2016/article-5</code></td>
  </tr>
  <tr>
    <td>Model laws / legislation</td>
    <td><a href="https://www.achpr.org/legalinstruments/detail?id=32">Model Law on Access to Information for Africa, 2013</a></td>
    <td>model-law</td>
    <td><code>/akn/aa/statement/model-law/achpr/2013/access-to-information</code></td>
  </tr>
  <tr>
    <td>Principles</td>
    <td><a href="https://www.achpr.org/legalinstruments/detail?id=2">Principles on the Decriminalisation of Petty Offences in Africa</a></td>
    <td>principles</td>
    <td><code>/akn/aa/statement/principles/achpr/2017/decriminalisation-petty-offences</code></td>
  </tr>
  <tr>
    <td>Recommendation</td>
    <td><a href="https://www.achpr.org/adoptedresolution">Recommendation on Periodic Reports</a></td>
    <td>recommendation</td>
    <td><code>/akn/aa/statement/recommendation/achpr/1998/3-3</code> <br>
(third session, recommendation 3)</td>
  </tr>
  <tr>
    <td>Resolution</td>
    <td>Resolution on the Military</td>
    <td>resolution</td>
    <td><code>/akn/aa/statement/resolution/achpr/1994/16-10</code> <br>
(sixteenth session, resolution 10)</td>
  </tr>
</table>

#### Documents with the <code>judgment</code> doctype

<table class="table table-sm table-bordered">
  <tr>
    <th>Document type</th>
    <th>Example</th>
    <th>Subtype</th>
    <th>FRBR URI</th>
  </tr>
  <tr>
    <th colspan="5">Other documents</th>
  </tr>
  <tr>
    <td>Judgment</td>
    <td>Judgment 5 of 2019 from the Kenyan High Court</td>
    <td></td>
    <td><code>/akn/ke/judgment/kehc/2019/5</code></td>
  </tr>
</table>

#### Documents with the <code>doc</code> doctype

<table class="table table-sm table-bordered">
  <tr>
    <th>Document type</th>
    <th>Example</th>
    <th>Subtype</th>
    <th>FRBR URI</th>
  </tr>
  <tr>
    <td>Policy</td>
    <td><a href="https://www.sadc.int/documents-publications/show/823">SADC Regional Water Policy</a></td>
    <td>policy</td>
    <td><code>/akn/aa-sadc/doc/policy/2005/water</code></td>
  </tr>
  <tr>
    <td rowspan="2">Policy Framework</td>
    <td><a href="https://www.achpr.org/legalinstruments/detail?id=25">Policy Framework for Pastoralism in Africa</a></td>
    <td rowspan="2">policy-framework</td>
    <td><code>/akn/aa/doc/policy-framework/auc-department-of-rural-economy-and-agriculture/2010/pastoralism</code></td>
  </tr>
  <tr>
    <td><a href="https://www.achpr.org/legalinstruments/detail?id=23">Framework and Guidelines* on Land Policy in Africa</a> <br>
* While the phrase ‘policy framework’ does appear in the document, we stand to be corrected on whether this document should fall under a different subtype, potentially ‘statement/framework-and-guidelines’. We hesitate to create subtypes that only include one document, but this may be an instance where it makes sense to do so.</td>
    <td><code>/akn/aa/doc/policy-framework/auc-uneca-afdb-consortium/2010/land</code></td>
  </tr>
  <tr>
    <td>Study</td>
    <td><a href="https://www.achpr.org/legalinstruments/detail?id=66">Study on Transitional Justice and Human and Peoples’ Rights in Africa</a></td>
    <td>study</td>
    <td><code>/akn/aa/doc/study/achpr/2018/transitional-justice-and-human-and-peoples-rights</code></td>
  </tr>
  <tr>
    <td>Yearbook</td>
    <td><a href="https://www.achpr.org/legalinstruments/detail?id=70">African Human Rights Yearbook Volume 3 (2019)</a></td>
    <td>yearbook</td>
    <td><code>/akn/aa/doc/yearbook/achpr/2019/3</code></td>
  </tr>
</table>

#### Documents with the <code>documentCollection</code> doctype

<table class="table table-sm table-bordered">
  <tr>
    <th>Document type</th>
    <th>Example</th>
    <th>Subtype</th>
    <th>FRBR URI</th>
  </tr>
  <tr>
    <td>Texts</td>
    <td><a href="https://au.int/en/treaties/regulatory-and-instutional-texts-implementation-yamoussoukro-decision-and-framework-towards">Regulatory and Institutional Texts for the Implementation of the Yamoussoukro Decision and Framework Towards the Establishment of a Single African Air Transport Market</a></td>
    <td>texts</td>
    <td><code>/akn/aa/documentCollection/texts/austc-transport-infrastructure-energy-tourism/nd/implementation-of-the-yamoussoukro-decision</code></td>
  </tr>
</table>


### Country legislation

This non-exhaustive table is based on our experience with legislation from the jurisdictions listed below. We’ve mostly worked with only the English documents from these jurisdictions so far.

We’ll therefore very likely be adding to this table in future, but barring a major overhaul we won’t change what’s in it so far.

You may notice that only `act` is used as the doctype; this is because our focus within countries has been only on gazetted legislation, for which we will always use `act`.

These countries have helped informed this table:

* Botswana
* Ghana
* Kenya
* Lesotho
* Malawi
* Mauritius
* Namibia
* Nigeria
* South Africa
* Tanzania
* Uganda
* Zambia
* Zimbabwe

<table class="table table-sm table-bordered">
  <tr>
    <th>Document type</th>
    <th>Example</th>
    <th>Subtype</th>
    <th>FRBR URI</th>
  </tr>
  <tr>
    <td>Act</td>
    <td><a href="https://commons.laws.africa/akn/ng/act/1993/73/eng@2002-12-31">Nigeria Social Insurance Trust Fund Act 73 of 1993 (Nigeria)</a></td>
    <td> </td>
    <td><code>/akn/ng/act/1993/73</code></td>
  </tr>
  <tr>
    <td>Board Notice</td>
    <td><a href="https://commons.laws.africa/akn/za/act/bn/2020/85/eng@2020-07-31">Directions Regarding Livestock Auctions (Board Notice 85 of 2020) (South Africa)</a></td>
    <td>bn</td>
    <td><code>/akn/za/act/bn/2020/85</code></td>
  </tr>
  <tr>
    <td>By-law</td>
    <td><a href="https://mbizana.openbylaws.org.za/za-ec443/act/by-law/2017/temporary-advertisements/eng/">Control of Temporary Advertisements By-law (Mbizana Municipality, South Africa)</a></td>
    <td>by-law</td>
    <td><code>/akn/za-ec443/act/by-law/2017/temporary-advertisements</code></td>
  </tr>
  <tr>
    <td>Constitution</td>
    <td><a href="https://namiblii.org/akn/na/act/1990/constitution">Namibian Constitution (Namibia)</a></td>
    <td></td>
    <td><code>/akn/na/act/1990/constitution</code></td>
  </tr>
  <tr>
    <td>Constitutional Instrument</td>
    <td>None found</td>
    <td>ci</td>
    <td></td>
  </tr>
  <tr>
    <td>Corrigendum</td>
    <td>None found</td>
    <td>corr</td>
    <td></td>
  </tr>
  <tr>
    <td>Decree</td>
    <td><a href="https://ulii.org/akn/ug/act/decree/1976/18/">Interpretation Act (Chapter 3, Decree 18 of 1976) (Uganda)</a></td>
    <td>decree</td>
    <td><code>/akn/ug/act/decree/1976/18</code></td>
  </tr>
  <tr>
    <td>Executive Instrument</td>
    <td><a href="https://commons.laws.africa/akn/gh/act/ei/2020/68/eng@2020-04-17">Imposition of Restrictions (Coronavirus Disease (COVID-19) Pandemic) (No. 5) Instrument, 2020 (Executive Instrument 68 of 2020) (Ghana)</a></td>
    <td>ei</td>
    <td><code>/akn/gh/act/ei/2020/68</code></td>
  </tr>
  <tr>
    <td>General Notice</td>
    <td><a href="https://commons.laws.africa/akn/mu/act/genn/2020/1937/eng@2020-11-27">Order under Section 3(1)(a) of the Quarantine Act 2020: Prohibition of Aircraft and Ships into Mauritius (General Notice 1937 of 2020) (Mauritius)</a></td>
    <td>genn</td>
    <td><code>/akn/mu/act/genn/2020/1937</code></td>
  </tr>
  <tr>
    <td>Government Notice</td>
    <td><a href="https://commons.laws.africa/akn/mw/act/gn/2020/48/eng@2020-08-07">Public Health (Corona Virus and COVID-19) (Prevention, Containment and Management) Rules, 2020 (Government Notice 48 of 2020) (Malawi)</a></td>
    <td>gn</td>
    <td><code>/akn/mw/act/gn/2020/48</code></td>
  </tr>
  <tr>
    <td>Legal Notice</td>
    <td><a href="https://commons.laws.africa/akn/ls/act/ln/2020/38/eng@2020-04-22">Public Health (COVID-19) Regulations, 2020 (Legal Notice 38 of 2020) (Lesotho)</a></td>
    <td>ln</td>
    <td><code>/akn/ls/act/ln/2020/38</code></td>
  </tr>
  <tr>
    <td>Legislative Instrument</td>
    <td><a href="https://commons.laws.africa/akn/gh/act/li/2007/1833/eng@2007-06-08">Labour Regulation, 2007 (Legislative Instrument 1833 of 2007) (Ghana)</a></td>
    <td>li</td>
    <td><code>/akn/gh/act/li/2007/1833</code></td>
  </tr>
  <tr>
    <td>Local Authority Notice</td>
    <td><a href="https://openbylaws.org.za/za-jhb/act/lan/2008/1628/eng/">Rights of Way for Electronic Communications Facilities (Local Authority Notice 1628 of 2008) (Johannesburg Municipality, South Africa)</a></td>
    <td>lan</td>
    <td><code>/akn/za-jhb/act/lan/2008/1628</code></td>
  </tr>
  <tr>
    <td>Ministerial Order</td>
    <td><a href="https://commons.laws.africa/akn/za/act/mo/2020/civil-aviation-authority-covid-19/eng@2020-03-18">Ministerial Order: South African Civil Aviation Authority (Unnumbered Ministerial Order, 2020) (South Africa)</a></td>
    <td>mo</td>
    <td><code>/akn/za/act/mo/2020/civil-aviation-authority-covid-19</code></td>
  </tr>
  <tr>
    <td>Municipal Notice</td>
    <td><a href="https://commons.laws.africa/akn/za-eth/act/mn/1999/7/eng@1999-02-04">Electricity Supply By-law (Durban Transitional Metropolitan Council): Correction (Municipal Notice 7 of 1999) (eThekwini Municipality, South Africa)</a></td>
    <td>mn</td>
    <td><code>/akn/za-eth/act/mn/1999/7</code></td>
  </tr>
  <tr>
    <td>Official Notice</td>
    <td><a href="https://commons.laws.africa/akn/za-mp/act/on/1999/2/eng@1999-01-29">Mpumalanga Nature Conservation Regulations, 1999 (Official Notice 2 of 1999) (Mpumalanga Province, South Africa)</a></td>
    <td>on</td>
    <td><code>/akn/za-mp/act/on/1999/2</code></td>
  </tr>
  <tr>
    <td>Ordinance</td>
    <td><a href="https://ulii.org/akn/ug/act/ord/1961/4/">Foreign Judgments (Reciprocal Enforcement) Act (Chapter 9, Ordinance 4 of 1961) (Uganda)</a></td>
    <td>ord</td>
    <td><code>/akn/ug/act/ord/1961/4</code></td>
  </tr>
  <tr>
    <td>Premier’s Notice</td>
    <td><a href="https://commons.laws.africa/akn/za-mp/act/premn/1999/1/eng@1999-01-04">Mpumalanga Nature Conservation Act, 1998: Commencement (Premier’s Notice 1 of 1999) (Mpumalanga Province, South Africa)</a></td>
    <td>premn</td>
    <td><code>/akn/za-mp/act/premn/1999/1</code></td>
  </tr>
  <tr>
    <td>Proclamation</td>
    <td><a href="https://namiblii.org/akn/na/act/p/2020/26/">Stage 3: COVID-19 Regulations: Erongo Region (Proclamation 26 of 2020) (Namibia)</a></td>
    <td>p</td>
    <td><code>/akn/na/act/p/2020/26</code></td>
  </tr>
  <tr>
    <td>Provincial Notice</td>
    <td><a href="https://commons.laws.africa/akn/za-kzn/act/pn/2012/64/eng@2013-07-11">KwaZulu-Natal Gaming and Betting Regulations, 2012 (Provincial Notice 64 of 2012) (KwaZulu-Natal Province, South Africa)</a></td>
    <td>pn</td>
    <td><code>/akn/za-kzn/act/pn/2012/64</code></td>
  </tr>
  <tr>
    <td>Statute</td>
    <td><a href="https://ulii.org/akn/ug/act/statute/1996/13/">Judicature Act (Chapter 13, Statute 13 of 1996) (Uganda)</a></td>
    <td>statute</td>
    <td><code>/akn/ug/act/statute/1996/13</code></td>
  </tr>
  <tr>
    <td>Statutory Instrument</td>
    <td><a href="https://commons.laws.africa/akn/bw/act/si/2016/45/eng@2016-04-22">Electronic Records (Evidence) (Date of Commencement) Order, 2016 (Statutory Instrument 45 of 2016) (Botswana)</a></td>
    <td>si</td>
    <td><code>/akn/bw/act/si/2016/45</code></td>
  </tr>
</table>
