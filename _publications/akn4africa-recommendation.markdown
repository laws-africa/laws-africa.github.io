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
* Akoma Ntoso Naming Convention: http://docs.oasis-open.org/legaldocml/akn-nc/v1.0/akn-nc-v1.0.html
* AKN4UN: https://unsceb-hlcm.github.io/
* AKN4EU: https://op.europa.eu/en/web/eu-vocabularies/akn4eu

# Generating FRBR URIs

AKN FRBR URIs are constructed as follows, with the italics text indicating that an element is optional:
> /akn/{2-letter country code-locality code}/{doctype}/{subtype}/{author}/{year}/{number}
In general, lowercase all letters and don’t use any spaces.
The sections below go into detail about each of the FRBR URI elements. Before that, we outline our guiding principles when deciding how to structure FRBR URIs in a given jurisdiction.
At the end are example FRBR URIs for regional and country legislation. We have aimed to include an example for each doctype and subtype.


















| Body                                                                                                                              | Author code                                      |
|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| African Commission on Human and Peoples’ Rights                                                                                   | achpr                                            |
| African Union Commission                                                                                                          | auc                                              |
| African Union Specialized Technical Committee on Transport, Transcontinental and Interregional Infrastructure, Energy and Tourism | austc-on-transport-infrastructure-energy-tourism |
| Committee for the Prevention of Torture in Africa                                                                                 | cpta                                             |
| Department of Rural Economy and Agriculture of the African Union Commission                                                       | auc-department-of-rural-economy-and-agriculture  |
| Organisation of African Unity                                                                                                     | oau                                              |


