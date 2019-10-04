---
title: Machine-friendly legislation – who’s doing what
date: 2019-10-04 10:24:00 +02:00
author: Edith V
image: "/uploads/leaves.jpg"
lead: A sample of tools and projects in the field of machine-friendly legislation
---

I recently attended the [Lex Summer School](http://summerschoollex.cirsfid.unibo.it/) and Akoma Ntoso Developers Workshop at the Law Faculty of the University of Bologna in Ravenna, Italy, where a jam-packed schedule introduced attendees to everything from marking up legislation by hand to using machine learning to extract knowledge from legal text. Below is a sample of current projects creating / working with machine-friendly legislation. (Note: AKN can be used for all kinds of legal texts, not just legislation; I’m just focusing on legislation because [that’s what we do](https://laws.africa/).)

While [Akoma Ntoso](http://www.akomantoso.org/) (AKN) has been around in different guises for about a decade, it is a nascent standard, having been officially accepted by OASIS in August 2018. People are working with AKN in the ways that make most sense to their contexts, and it’s a strength of the standard that there isn’t One Right Way to produce and work with valid AKN.

Having legal text marked up in AKN unlocks the potential to work with the text in a more meaningful (and efficient) way. While improved search and cross-referencing alone may well be worth the trouble of converting existing legal corpuses into AKN, we can also take it a step or two further: creating links between concepts, marking up legal rules, and testing a body of rules for internal consistency. To those of us working towards access to the text itself, this is more of theoretical interest than of immediate practical application, but the work already being done in this space in other places gives us a glimpse into what is possible once the hard slog of converting legal text into AKN has been done.

# Official AKN projects

## FRBR URI resolver

Legislation changes over time, so a vague reference to a given Act is deceptively simple: the Act as it stood on the date this other document was produced? when it was published? or the most recent version? and in which language? Where multiple versions of a piece of legislation are available and only some of the reference information is given (say the Act year and number, but not the language), the resolver makes some informed guesses as to which one is meant (but gives the option to switch as well). Check out the demo here: [http://akresolver.cs.unibo.it/](http://akresolver.cs.unibo.it/) (Tip: once you’ve clicked through to a ‘resolved’ version, click on the AKN logo in the corner.)

## Subschema generator

AKN is a large standard with very many elements and a pretty low barrier to validity. It doesn’t care if you have parts inside sections – a bonkers idea in the South African tradition, but perfectly valid in the US – precisely because what is bonkers to you and me is perfectly valid elsewhere. That also means, however, that it’s possible to produce a valid AKN document that doesn’t conform to the local tradition. One of a few ways of addressing this is to create a subschema, which when validated will check for valid AKN as well as any constraints you may want to add on top, e.g. ‘sections must have headings’ or ‘chapters may contain parts and sections, but no standalone text’. A user-friendly way of generating such a subschema can be found here: [http://akn.web.cs.unibo.it/akgenerator/](http://akn.web.cs.unibo.it/akgenerator/).

## LIME – Language-Independent Markup Editor

LIME allows a human editor familiar with their local legal traditions to mark up legal text without hand-coding the XML. It includes an ‘Automatic markup’ functionality that will guess at elements like sections, parts, definitions, etc., and a human can then go through and add/correct as necessary. See for yourself here: [http://sinatra.cirsfid.unibo.it/lime-lex/](http://sinatra.cirsfid.unibo.it/lime-lex/).

## RAWE – LegalRuleML rules designer

LegalRuleML is a (you guessed it) markdown language for modelling logic rules inferred from legal texts. RAWE allows a human to construct such rules visually, using Scratch: [http://sinatra.cirsfid.unibo.it/rawe-legregsw/](http://sinatra.cirsfid.unibo.it/rawe-legregsw/).

# Other editors

* Laws.Africa: The [Indigo](https://github.com/laws-africa/indigo/) editor

* Xcential: [LegisPro](https://xcential.com/legispro-xml-tech/)

* Bungeni Consulting: [BungeniX](https://www.bungeni.com/text_to_akomantoso.html) (conversion) and [BungeniEd](https://www.bungeni.com/legislative_drafting.html) (editing)

* European Commission: [LEOS](https://ec.europa.eu/isa2/solutions/leos_en)

# Other cool projects and tools

* [Sankofa](https://gitlab.com/CIRSFID/un-challange-2019/blob/master/documents/project.md)

* [Akomando](http://www.akomando.bitnomos.eu/)

* [LRML Search](https://tal.lipn.univ-paris13.fr/LexEx)