# stream_3
Final Project for Stream 3

This app takes the original CandyLand website and re-builds it using greater functionality utilising
integrated front-end and back-end components together to create a better, more inclusive user
experience.

## Key Features

As well as the usual "Take a look at what we do", of the initial website, things have moved on so now
you can:

* Visit social media outlets for the Candyland Cart Company and see what's happening.
* Make a booking request detailing how you would like the company to cater for your needs.
* Register as a member of the Candy Club to get news and obtain discounts on bookings.
* As a member, you are able to purchase sweet packages directly from the site.
* In addition, you can also take out a "Sweet Subscription", enabling you to have a sweet hamper
  delivered to you on a monthly basis.
* Take part in surveys / polls about sweet related stuff and post up a review thread on an event you
  may have booked or attended and even set up your own opinion poll.

## How does this one work?

This app uses the following tech to do its thing:

* Django and Python does all the heavy lifting framework wise and keeps everything both linked up AND nicely
  separated at the same time.
* HTML5.
* CSS.
* Bootstrap for styling and ensuring cross browser and multi-display compatibility.
* PayPal to manage one-off payments and subscription services.
* Whitenoise to allow you to serve your own static files (CSS, JS, Images etc.), meaning the projet is fully
self-contained.
* db.sqlite3 enables new user details to be stored and retrieved for authentication purposes, as well as
storing comments on review treads and posts in the members forum.

## What's going on?

There's a lot going on here but put simply, the project is divided into separate but inter-dependant
applications. Member registration is handled by the "Accounts" app, general layout is taken care of using
"CandylandApp_app", "paypal_store" takes care of purchases etc. etc. This means that each section can be worked
on by itself and integrated at a later stage when complete.

## Contribute to this project

If you feel you would like to develop this further you are more then welcome to. Just clone this repository
by running the `git clone https://github.com/bugdude01/candyland2` command. Once you have that in place make
sure you install the requirements in the requirements/base.txt folder and away tou go!

Feel free so share any findings you have, suggested improvements etc., as all suggestions are welcome. Also, if
you find any bugs / issues, please let me know. We are all learning all the time and no developer should be an
island - It's very lonely that way!

## See things running "Live" - take a look here: https://candyland2.herokuapp.com
