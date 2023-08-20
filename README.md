# flyUX-pp4

# Project Background

- This project represents an opportunity to showcase my skills in both UX design and web development, bridging the gap between form and function. 
- This Django web development project is a continuation of a UX Design project I completed during my Diploma with the UX Design Institute which goes through the full UX process from research all the way to prototyping and handover.
- The end result was a user-friendly flight booking flow which was informed by user research and prototyped to a medium fidelity in Figma.
- Revisiting the project a year later, I am now using it as a foundation to build upon and bring it from Figma prototype, to a fully functioning Django-based web application, combining my passions for user-centric design and web development to build a holistic solution.


# Bugs
1. When styling the flight search result cards, there was some difficulty in adding a transition to animate the expansion of the card when clicked, to show the fares. It was found that it is not possible to transition from `display:hidden`, nor is it possible to transition from heigh:0 to height:auto. A workaround was implemented by setting `max-height:0` with `overflow:hidden` then using JavaScript to add `max-height:100rem` (or any other large value) along with `transition:all` to animate the card expansion and collapse.
2. The "alternate date selector" on the flight results page works by sending an AJAX request (via htmx) when an alternate date is clicked, and responding with HTML with the new flight data for the given date. When the new HTML is loaded from the response, the click event listeners need to be re-attached to the new flight card elements so that they expand when clicked, to show the fares. However, when initially trying to implement this re-attachment, an issue arose where the flight cards would not expand every second time an alternate date was selected. Following some troubleshooting, it was found that the click event listeners were compounding, thus negating each other (i.e. as if a user clicked the card twice in rapid succession). Using `console.log` and Chrome Dev Tools for debugging enabled me to see which events were firing so that the issue could be identified and solved by defining the click handler function outside of the event listner function. [Relevant Stack Overflow thread.](https://stackoverflow.com/questions/41720943/rebind-javascript-events-and-addeventlistener-fires-twice)
3.  The `Flight`s table contains 90,000 rows of data and when implementing the `Booking`s CRUD functionality, there were severe issues experienced particularly in the admin panel when trying to view/edit `Booking`s which resulted in indefinite loading times as the `Flight`s data was loaded. Django has a number of built-in solutions for this issue and a solution was implemented by defining `search_fields` and `autocomplete_fields` in the `ModelAdmin` configurations for the `Flight` and `Booking` models. [Django Documentation Reference](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.autocomplete_fields)
4. When testing the site on mobile, a bug was identified where the date input field placeholder text would not display. Following some research and troubleshooting, it was found that this is a known issue with Flatpickr and a workaround was found as [referenced in this JSfiddle](https://jsfiddle.net/Sova12309/7bmpy9jc/9/).

<details>
<summary>Code Snippet Implemented</summary>

```css

.flatpickr-mobile:before {
    content: attr(placeholder);
    color: #9ca3af;
    width:100%;
    }

.flatpickr-mobile:focus[value]:not([value=""]):before {
    display: none;
    }
    
input[type="hidden"][value]:not([value=""]) + .flatpickr-mobile:before {
    display: none; 
    }

```

</details>

---

## Technologies Used
This section outlines the various technologies used throughout the project and the purpose each serves.

### Core Development Technologies
- [Django](https://www.djangoproject.com/) used as a full-stack framwork for developing the app.
- [JavaScript](https://www.ecma-international.org/publications-and-standards/standards/ecma-262/) used for client-side interaction and validation.
- [HTML](https://html.spec.whatwg.org/)/[CSS](https://www.w3.org/Style/CSS/Overview.en.html) + [Django Template Language](https://docs.djangoproject.com/en/4.2/ref/templates/language/) used for building out site pages.

### Libraries, Frameworks and Packages
- [Tailwind CSS](https://tailwindcss.com/) - used to style elements throughout the site.
- [Flowbite](https://htmx.org/) - a Tailwind-based open-source library; used very sparingly for small number of minor components in the site (radio select, dropdown select)
- [htmx](https://htmx.org/) - an open-source lightweight library used to fetch and load content dynamically via AJAX requests. Utilised specifically for fetching new `Flight` data and `Passenger`s edit form.
- [Flatpickr](https://flatpickr.js.org/) - a JavaScript library which provides the date picker styles and functionality on the Homepage.
- [Payform](https://github.com/jondavidjohn/payform) - a JavaScript library used for formatting the Payment Details form inputs.

#### Python/Django Packages
- [Gunicorn](https://pypi.org/project/gunicorn/) - provides HTTP server
- [psycopg2](https://pypi.org/project/psycopg2/) - provides PostgreSQL connection
- [Pillow](https://pypi.org/project/Pillow/) - used for image processing (Model ImageField)
- [Whitenoise](https://pypi.org/project/whitenoise/) - used for serving static files
- [Coverage](https://pypi.org/project/coverage/) - used for testing and analysis
- [Django Markdown Field](https://pypi.org/project/django-markdownfield/) - adds a markdown-compatible text field to admin panel (for BlogPost model)

### Infrastructural Technologies
- [PostgreSQL](https://www.postgresql.org/) (via Digital Ocean) - used for database.
- [Heroku](https://www.heroku.com/) - used for hosting the application.

# Testing
## Automatic Testing
- Automated unit tests were written for core back-end functionality of the app to test data validation and integrity, templates used, HTTP status codes, user input etc.
- 35 tests were written in total.
- The [`Coverage`](https://pypi.org/project/coverage/) package was used to assist in guiding test requirements. 
- 100% coverage was achieved on the `core` models and views.
- Future plans to write unit tests for coverage on `blog` and `users` apps.

## Manual Testing



# Credits
- [Unsplash](https://unsplash.com/) - used for sourcing Blog photographic images.
- [ChatGPT](https://openai.com/chatgpt) - used for generating all Blog text content.
- [Favicon.io](https://favicon.io/) - used to create favicon.
- [Payform](https://github.com/jondavidjohn/payform) - used for Payment Details input formatting.
- [Mockaroo](https://www.mockaroo.com/) - used for creating model data.