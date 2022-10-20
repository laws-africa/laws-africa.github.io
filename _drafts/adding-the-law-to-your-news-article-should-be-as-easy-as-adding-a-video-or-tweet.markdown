---
title: Adding the law to your news article should be as easy as adding a video or
  tweet
date: 2022-08-23 09:51:00 +02:00
author: Greg Kempe
lead: 'Call for early adopters: help your readers by embedding legislation into your
  articles just as you would embed a tweet.'
---

<style>
la-akoma-ntoso {
  background-color: #efefef;
  padding: 0.5em 1em;
  margin-bottom: 1em;
  max-height: 50vh;
  overflow-y: auto;
}
</style>

We're looking for early testers to try out our new "Embed the Law" widget. Our new widget makes it easy to embed legislation into your website, just as you would embed a video or tweet.

If you're a South African news outlet or non-profit organisation that publishes articles or blog posts that mention legislation, we'd like to partner with you to explore how to make it easier for your readers to learn about the law.

## Providing context to your readers

Many news outlets and blogs embed content into their articles to provide context and background for their readers. Embedded content includes images, videos, tweets, documents and audio recordings. This content forms a part of the story and makes for a richer experience for the reader.

We want to help these organisations enrich their stories by embedding the law. Embedding a paragraph, section, chapter or even an entire piece of legislation can provide context and support for a story.

## What it looks like

You can embed just a particular provision (chapter, part, section, paragraph) of a piece of legislation. Here is Section 5 of the [Prevention of Organised Crime Act (Act 121 of 1998)](https://lawlibrary.org.za/akn/za/act/1998/121/eng@2016-06-01):

<la-akoma-ntoso fetch partner="laws.africa" frbr-expression-uri="/akn/za/act/1998/121/eng@2016-06-01/~chp_3__sec_5"></la-akoma-ntoso>

You can also embed an entire piece of legislation. These can be pretty big, so you may want to add CSS to limit the height and make it scroll. Here is the entire [General Notice 629 of 2021](https://lawlibrary.org.za/akn/za/act/genn/2021/629/eng@2021-10-22):

<la-akoma-ntoso fetch partner="laws.africa" frbr-expression-uri="/akn/za/act/genn/2021/629/eng@2021-10-22"></la-akoma-ntoso>

## How it works

Embedding legislation requires three easy steps:

1. Add a javascript library to your page
2. Determine the legislation and provision you want to embed
3. Add the `<la-akoma-ntoso>` embed element, for example:

```html
<la-akoma-ntoso
  fetch
  frbr-expression-uri="/akn/za/act/1998/121/eng@2016-06-01/~chp_3__sec_5"
></la-akoma-ntoso>
```

The element fetches the content from the Laws.Africa servers and includes it in your page. Done!

### How it works: for the techies

The javascript library registers a [web component](https://developer.mozilla.org/en-US/docs/Web/Web_Components). The embedding code uses this new web component to load the content from the Laws.Africa server into your page. Instead of using an iframe, the content is rendered inside the of the element. This gives you the flexibility of using CSS to style the content.

In the examples above, we've applied this CSS:

```css
la-akoma-ntoso {
  background-color: #efefef;
  padding: 0.5em 1em;
  margin-bottom: 1em;
  max-height: 50vh;
  overflow-y: auto;
}
```

## Sign me up! I want to help my users read and understand the law.

We're currently beta testing this functionality with South African news outlets. Please get in touch with Greg Kempe by email at [greg@laws.africa](mailto:greg@laws.africa) and we'll help you get set up.
