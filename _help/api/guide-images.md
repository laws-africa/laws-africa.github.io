---
title: 'API Guide: Downloading Images'
position: 3
lead: Downloading embedded images from the Laws.Africa Content API.
---

This guide will take you through how to work with images and other media embedded in expressions in Laws.Africa’s Content API. After reading this guide you will know:

* how to list all the images and media included with an expression
* how to download and save images and other media from the Content API
* how to ensure that images are loaded correctly in your HTML content

# What are embedded images?

Some legislation includes embedded images. You will need to download and store these images to ensure they are displayed when you show the legislation to your users.

You must download these images to include them in your HTML. The images will not be shown from the Laws.Africa servers.
{:.alert.alert-info}

# Including images in your application or website

There are two steps to include embedded images in the legislation used in your app or website.

1. Download the images from the Laws.Africa Content API and save them to your server or app.
2. Ensure the HTML you fetch from the Laws.Africa Content API references the images correctly.

We'll go through each of these steps below.

# How to list images using the Content API

The Laws.Africa Content API makes it easy to list and download embedded images for a particular work. Fetch the list of images using the `/frbr-uri/media.json` URL for the work. You can find this URL in the work's `links` array:

```json
"links": [
  {
    "mediaType": "application/json",
    "href": "https://api.laws.africa/v2/akn/za-jhb/act/by-law/2004/public-road-electronic-communications-networks-and-miscellaneous/eng/media.json",
    "title": "Media",
    "rel": "media"
  },
]
```

For example, here is the API call to list the images embedded with Johannesburg's [Public Road and Miscellaneous By-laws by-law](https://openbylaws.org.za/za-jhb/act/by-law/2004/public-road-electronic-communications-networks-and-miscellaneous/eng/):

```bash
$ curl -H "Authorization: Token <YOUR_AUTH_TOKEN>" \
  https://api.laws.africa/v2/akn/za-jhb/act/by-law/2004/public-road-electronic-communications-networks-and-miscellaneous/media.json
```

```json
{
  "count": 10,
  "next": null,
  "previous": null,
  "results": [
    {
      "url": "https://api.laws.africa/v2/akn/za-jhb/act/by-law/2004/public-road-electronic-communications-networks-and-miscellaneous/eng@2011-08-10/media/certificate.png",
      "filename": "certificate.png",
      "mime_type": "image/png",
      "size": 253224
    },
    {
      "url": "https://api.laws.africa/v2/akn/za-jhb/act/by-law/2004/public-road-electronic-communications-networks-and-miscellaneous/eng@2011-08-10/media/indemnity.png",
      "filename": "indemnity.png",
      "mime_type": "image/png",
      "size": 210645
    },
  ]
}
```

Each item in the list describes a single image or media type and includes the filename, [mime type](https://en.wikipedia.org/wiki/Media_type), filesize in bytes, and the URL to use to download the file.

# Downloading and saving images

In order for the embedded images to show up when your users view the content you have fetched from the Laws.Africa API, you must first download and store the images
locally.

You must save the images in a folder called `media`, next to your legislation HTML file. The `<img>` tags in the HTML will try to load the images from this path.
{:.alert.alert-info}

For example, suppose you have downloaded the English HTML content of the 2011-08-10 point in time for the by-law and saved it as:

* `public-road-electronic-communications-networks-and-miscellaneous/eng/2011-08-10/index.html`

Then you should download and save the media files to `media` folder in the same directory:

* `public-road-electronic-communications-networks-and-miscellaneous/eng/2011-08-10/media/`

This ensures that you'll keep the different images for different works, languages and points in time separate.

You must save the images separately for each separate point in time and language that you download.
{:.alert.alert-info}

# Controlling where images are loaded from

By default, HTML from Laws.Africa will try to load images from the `media` directory relative to the current URL, using an image tag such as `<img src="media/wayleave-application.png">`.

If you need to load images from a different location you can tell Laws.Africa to use apply a prefix to the `src` attribute of image tags by using the `?media-url` query parameter.

For example, using `?media-url=/static/assets/za/act/1995/2/eng/2018-11-10/` will produce image tags such as `<img src="/static/assets/za/act/1995/2/eng/2018-11-10/media/wayleave-application.png">`.

You should encode the FRBR URI into the `media-url` parameter to ensure that you show images for the correct work, point in time and language.
{:.alert.alert-info}
