---
title: Country codes in FRBR URIs
date: 2021-07-27 10:10:00 +02:00
author: Edith V
lead: It’s straightforward, until it isn’t!
image: "/uploads/lina-loos-04-C1NZk1hE-unsplash-6e5ae5.jpg"
---

*This series of blog posts goes into some of the edge cases Laws.Africa encountered as we started applying the AKN Naming Convention to African legislation. Read the full [AKN4Africa Recommendation](https://laws.africa/publications/akn4africa-recommendation.html).*

After the universal `akn` prefix, which indicates that this is an FRBR URI under the AKN Naming Convention, the first variable element of a work’s FRBR URI is the ‘country or subdivision’.

This blog post explains how we grappled with the constraint that this must be a two-letter code under ISO 3166 when working with regional African bodies.

### The simple case: Countries

For literal countries, we use the two-letter ISO 3166-1 code as prescribed by the AKN Naming Convention. Within a country, we use the official codes assigned to provinces, municipalities, counties, and the like – ‘localities’ in our nomenclature. The code for the Mbizana municipality in South Africa, for example, is `za-ec443`.

### The trickier case: Regional bodies

Regional bodies in Africa – the African Union (AU), the East African Community (EAC), the Economic Community of West African States (ECOWAS), and the Southern African Development Community (SADC) – enact legislation, as well as model laws, resolutions, and other legislation-like documents, which member states adopt or refer to when enacting their own legislation. Case law also often refers to these laws or instruments.

None of these bodies have ISO 3166 codes, at least not yet. But we need to use a two-letter country code to be AKN compliant.

Below is a rough reconstruction of our decision-making process:

#### Option 1: ‘Other (xx)’

While working on a separate project in 2020, we introduced the country ‘Other’ on the laws.africa editorial platform for working with documents from decision-making bodies in a certain industry that aren’t tied to any country or regional body. The country code we used for ‘Other’ is `xx`, one of the codes that’s ‘free for assignment at the disposal of users’ under ISO 3166-1.

We could therefore simply prepend `xx-` and treat all regional bodies in Africa as localities within the country ‘Other’: `xx-au`, `xx-eac`, `xx-ecowas`, `xx-sadc`.

This, however, felt counter to the spirit of AKN, which aims to mark up legislation in a way that retains the semantics. (For example, sections in legislation are marked up as `"section"` rather than using a generic or non-human-friendly code.)

Moreover, lumping important African bodies that inform the legislative and regulatory landscape across the continent into 'Other' felt not only misleading but also disrespectful.

#### Option 2: ‘aa’

We decided, instead, to use one of the other 'free' codes from ISO 3166-1 for African bodies: `aa`.

Because it starts with an 'a' it's less random than 'xx', and this way regional African legislation doesn't end up being grouped under the same umbrella as other documents that don't have an obvious geographical home.

All regional bodies in Africa are thus prepended with ‘aa’: `aa-au`, `aa-eac`, `aa-ecowas`, and `aa-sadc`.

Initially, we used ‘aa’ as the code for the African Union, as the primary regional body in Africa. On further reflection, we decided to simply use ‘aa’ as an indicator that what follows is a regional body in Africa. The other bodies mentioned are after all not sub-bodies of the AU.

We published the second version of the [AKN4Africa Recommendation](https://laws.africa/publications/akn4africa-recommendation.html) on 26 July 2021 to reflect this change.

\(Photo of [World's End in Mpumalanga, South Africa](https://unsplash.com/photos/04-C1NZk1hE) by [Lina Loos](https://unsplash.com/@linaloos) from Unsplash.)