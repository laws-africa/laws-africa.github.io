---
title: AKN4Africa Recommendation
date: 2021-06-18 11:32:00 +02:00
published: false
header_class: bg-lawsafrica-pale-red
navbar_item: publications
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

AKN FRBR URIs are constructed as follows, with the *italics text* indicating that an element is optional:

/akn/{2-letter country code\*-locality code\*}/{doctype}*/{subtype}/{author}*/{year}/{number}

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

* The reference numbers of ACHPR Resolutions have the form ‘ACHPR/Res. 343(LVIII) 2016’. In AKN nomenclature this includes the author (`achpr`), the type (`resolution`), the number (`343`) and the year (`2016`). However, it also includes the session number, `58` (or LVIII). While it isn’t strictly necessary to include the number under the AKN Naming Convention, we include it in the FRBR URIs because it is commonly used when referring to ACHPR Resolutions: /akn/aa/statement/resolution/achpr/2016/\*\*58-\*\*343.

* ECOWAS documents are referred to as e.g. ‘A/SA.1/12/14’. The subtype (\`supplementary-act\`), year (\`2014\`) and number (\`1\`) are all included, as is the month in which the Supplementary Act was signed. The month isn’t strictly necessary to identify ‘Supplementary Act 1 of 2014’, but because it’s part of the local tradition, we include it in the FRBR URI: /akn/aa-ecowas/act/supplementary-act/2014/\*\*12-\*\*1.

When including information in FRBR URIs that isn’t strictly necessary, start with more general information and work your way to increasingly specific information (to the right of the FRBR URI) . When we include the session number for ACHPR Resolutions, and the month for ECOWAS documents, they come before the number itself, with a hyphen, because the number is the most specific element.

## Country code

Always use a 2-letter country code, whether the jurisdiction is a literal country or a regional body.

### Literal countries

For countries, use the ISO 3166[\[1\]](#ftnt1) 2-letter code, e.g. `ke` for Kenya.

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

For examples of doctypes and subtypes, see the Example FRBR URIs section.

### Doctype

* For legislation – Acts, Regulations, Statutory Instruments, and the like – use act.\
  These are documents that have the force of law.

* For soft law – Resolutions, Guidelines, Decisions, Model laws, Agreements, and the like – use statement.\
  These are documents that don’t (or only sometimes) have the force of law, but do still have to do with the law (to varying degrees).

* For case law, use judgment.

* For other documents – Policies, Memoranda of Understanding, Yearbooks, Press Releases, and the like – use doc.\
  This document, for example, would use the doc doctype.

| Body                                                                                                                              | Author code                                      |
|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| African Commission on Human and Peoples’ Rights                                                                                   | achpr                                            |
| African Union Commission                                                                                                          | auc                                              |
| African Union Specialized Technical Committee on Transport, Transcontinental and Interregional Infrastructure, Energy and Tourism | austc-on-transport-infrastructure-energy-tourism |
| Committee for the Prevention of Torture in Africa                                                                                 | cpta                                             |
| Department of Rural Economy and Agriculture of the African Union Commission                                                       | auc-department-of-rural-economy-and-agriculture  |
| Organisation of African Unity                                                                                                     | oau                                              |

---

[\[1\]](#ftnt_ref1) [https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2](https://www.google.com/url?q=https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)