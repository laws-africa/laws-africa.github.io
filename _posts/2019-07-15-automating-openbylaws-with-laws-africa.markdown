---
title: Automating OpenByLaws.org.za with Laws.Africa
date: 2019-07-15 15:06:00 +02:00
lead: How openbylaws.org.za uses Laws.Africa and “legislation as data” to automate
  the work of making municipal by-laws freely available.
author: Greg Kempe
image: "/uploads/cape-town-crane.jpg"
---

Municipal by-laws are part of the legal foundation of effective communities, small businesses, and local service delivery. However, they are often difficult to find, are out of date, or are in big PDF files that are difficult to work with.

[OpenByLaws.org.za](https://openbylaws.org.za) solves this problem by making South African by-laws easy to find, read and share. It includes the by-laws for a growing number of municipalities, including Cape Town, Johannesburg and eThekwini, and, through local partnerships, a number of smaller towns such as Cape Agulhas.

Open By-laws uses Laws.Africa to provide rich, interactive functionality to readers, and to automatically update its website every night. This means that it's quick and easy to make the by-laws available to residents, municipal staff, and law enforcement, using either computers or mobile phones.

## Quick and Easy: Legislation as Data

Open By-laws uses the [Laws.Africa Content API](https://laws.africa/api/) to automate website updates. Every night, Open By-laws automatically pulls in the latest by-laws from Laws.Africa and publishes them on the openbylaws.org.za website. This includes images, gazette information, inline definitions, and by-laws in HTML, PDF and ePUB formats.

<img src="/uploads/content-api.png" alt="Laws.Africa Content API diagram" class="img-fluid">

Traditionally, a website like Open By-laws would be painstakingly maintained by hand. Every change would require an editor to ensure that the headings are correctly formatted, the table of contents is updated, definitions are linked, and that the PDF version matches the webpage version.

The Laws.Africa Content API treats **legislation as data**, which means we can completely automate these tasks. Formatting is applied automatically, the table of contents is generated automatically, definitions are linked automatically, and the PDF versions are—you guessed it—generated automatically.

In addition, because the legislation is available as structured data (rather than as a Word document or a PDF), Open By-laws can add rich functionality. For example, specially defined terms are linked and their definitions are shown in a pop-up:

<img src="/uploads/bylaw-definitions.gif" alt="Inline definitions popup" class="img-fluid">

## What else can be done with the content API?

The [Laws.Africa Content API](https://laws.africa/api/) is very powerful. It provides a simple interface to extract and work with machine-friendly legislation, and associated metadata, using the open [Akoma Ntoso XML markup standard](http://www.akomantoso.org/).

Using the Content API, you can include African legislation in your website or app, [build interactive tools](https://laws.africa/help/api/guide-table-of-contents.html) to help users explore legislation relevant to them, or use machine learning to do research and analysis.

Find out more about the Laws.Africa Content API at [laws.africa/api](https://laws.africa/api/).

## Who keeps the by-laws up-to-date?

The Laws.Africa editors and contributor community keep the by-laws up-to-date. When new by-laws and amendments are published in the government gazettes, they are updated on the platform, reviewed, and made available through the Content API.

Anyone can become a contributor. Laws.Africa provides training, support and guidance. The work is divided into tasks that are clearly described and easy to do.

For example, here are the [tasks and by-laws for Cape Town](https://edit.laws.africa/places/za-cpt/).

<img src="/uploads/platform-cpt.png" class="img-fluid">

Contributions feed into the legislation commons which is freely available online, to everyone. [Apply to Laws.Africa to become a contributor](https://laws.africa/jobs) if you'd like to help out.

## Making even more by-laws freely available

Laws.Africa and Open By-laws are partnering with South African municipalities to put their by-laws online and provide training on how to maintain them on the Laws.Africa platform. If you're interested, please email [info@laws.africa](mailto:info@laws.africa).

You can find out more about how to use the Laws.Africa Content API in your website, app or research at [laws.africa/api](https://laws.africa/api/) or by emailing us at [info@laws.africa](mailto:info@laws.africa).

(Photo by Rohan Reddy on [Unsplash](https://unsplash.com/photos/Ae4qJD-IdL8).)