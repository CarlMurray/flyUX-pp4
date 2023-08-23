# flyUX-pp4

# 📄 Project Background

## 👀 Overview
- This Django web development project is a continuation of a UX Design project I completed during my Diploma in UX Design with the UX Design Institute which goes through the full UX process from user research all the way through to prototyping and handover.
- The end result was a user-friendly flight booking flow which was informed by user research and prototyped to a medium fidelity in Figma.
- Revisiting the project a year later, I am now using it as a foundation to build upon and bring it from Figma prototype, to a fully functioning Django-based full-stack web application, combining my passions for user-centric design and web development to build a holistic solution.

**[See here for the full UX Design case study](https://carlmurray.design/p/cmurray/03678e7f)**

# 🏗️ Process

## ❓ Problem Statement:

>Your client is a start-up airline. They’re looking to create an online experience that is fast, easy and intuitive: one that’s based on a deep understanding of their target users.

## 🔎 Research
- Competitive benchmarking was carried out to better understand what current industry leaders are doing and to understand common conventions and user expectations from a flight booking flow.
- Usability testing of existing flows were carried out with users on the Aer Lingus, Ryanair and EasyJet websites to observe user behaviour, mental models, positives and pain points. 
- This research data was used to inform my solution, which aimed to provide a simple, straight-forward, upsell-free and easy-to-use flight booking flow.

**[See here for the full UX Design case study](https://carlmurray.design/p/cmurray/03678e7f)**


## 🎨 Design
- Colour palette etc...

**[See here for the full UX Design case study](https://carlmurray.design/p/cmurray/03678e7f)**

## 👨‍💻 Development
- Agile...

## 🧮 Data Models
- Diagrams...



# 🪀 Features

## 💩 CRUD Functionality
- User CRUD functionality is primarily related to `Booking`s.
  - Create: Users create a Booking by going through the full user flow. A `Booking` is created once the user completes checkout.
  - Read: Users can view their created `Booking`s and relevant `Booking` details when logged in.
  - Update: Users can edit a `Booking` by changing `Passenger` information for that `Booking`.
  - Delete: Users can cancel a `Booking` which deletes it from the database.
- Admin CRUD functionality exists for all Models and is done from the Django Admin dashboard.

## 🔑 Authentication & Authorisation

- Users can create an account from the Signup page.
- Users can login from the Login page.
- Authorisation is required to reach certain pages such as Bookings, Passenger Details and Checkout. Requesting these pages while unauthprised will redirect users to the Login page. 
- If not logged in by the time a user reaches the Passenger Details page, a modal shows on screen with the Signup form. Users can also click the Login link at the bottom of the form instead, and be redirected to the Passenger Details page on successful authentication. 

<details>
<summary>Signup page</summary>

![Screenshot of Signup page](/readme/signup.jpeg)
</details>
<details>
<summary>Login page</summary>

![Screenshot of Login page](/readme/login.jpeg)
</details>
<details>
<summary>Signup modal</summary>

![Screenshot of Signup modal](/readme/signup-modal.jpeg)
</details>

## 🧭 Navigation
- Primary navigation is located in the header and is present on all pages.
- A hamburger menu is present on mobile devices and expands to show the primary navigation links.

<details>
<summary>Navigation on homepage</summary>

![Screenshot of homepage ](/readme/homepage.jpeg)
</details>


## 🔎 Search
- The search form is located on the homepage and allows users to search for flights by entering their origin, destination, trip type, dates and number of passengers.
- The search form is validated on the front-end and back-end to ensure that the data entered is valid and that the search can be performed.
- If the search is valid, the user is redirected to the Flights page where they can view the search results.
- If the search is invalid, an error message is shown.

<details>
<summary>Homepage with search form</summary>

![Screenshot of homepage](/readme/homepage.jpeg)
</details>

## ✈️ Flights
- The Flights page shows the search results for the user's search query.
- If there are no results, an info message is shown prompting the user to try an alternate date.
- If there are results, the results are shown in a card format with the outbound and return flights shown in separate cards.
- Once flights have been selected, the CTA button is enabled and the user can proceed to the next step in the booking flow. Selected flight numbers are stored in session storage and are used to populate the Order Summary page.
<details>
<summary>Flights</summary>

![Screenshot of Flights page](/readme/flights.jpeg)
</details>

### 🗓️ Alternate Dates
- The alternate dates feature allows users to view flight results for alternate dates to their original search query.
- The feature works by sending an AJAX request (via htmx) to the server with the new date, and the server responds with the new flight data for that date, and new date options for the alternate date selector.
- The new flight data is then loaded into the page and the click event listeners are re-attached to the new flight cards so that they expand when clicked, to show the fares.
- It is not possible to select a date that is in the past. 
- It is not possible to select a date that is before the outbound date if the trip type is return.

### 💸 Fares
- The fares are shown in a card format with the outbound and return fares shown in separate cards.
- The user can click on a fare card to expand it and show the fare details.
- The user can select a fare by clicking the button on the fare card.
- Selected fare information is stored in session storage and is used to populate the Order Summary page.

<details>
<summary>Fares</summary>

![Screenshot of Fares](/readme/flights-fares.jpeg)
</details>

### 🛫 Edit Flights
- The user can edit their flight selection by clicking the "Edit" button on the fare card.
- This reloads the previous flight search results and allows the user to select new flights.

<details>
<summary>Edit Flights</summary>

![Screenshot of Edit Flights](/readme/flights-fares.jpeg)
</details>

## 👯 Passengers
- The Passengers form is shown after the user has selected their flights.
- The form is pre-populated with the number of passengers selected in the search form.
- If logged in, the form is pre-populated with the user's details.
- The "Confirm email" field is not pre-populated and must be entered by the user as a security and error prevention measure.

<details>
<summary>Passengers form</summary>

![Screenshot of Passengers form](/readme/passengers.jpeg)
</details>

## 💳 Checkout
- The Checkout page shows the Order Summary and the Payment Details form.
- The Order Summary is populated with the flight and fare information stored in session storage.
- For the purposes of this project, the Payment Details form is a mockup and does not process any payments. The form is lightly validated on the front-end using the Payform library with some minor modification to allow for dummy card data to be entered.

<details>
<summary>Checkout page</summary>

![Screenshot of Checkout page](/readme/checkout.jpeg)
</details>


## ✅ Confirmation
- The Confirmation page shows the user's booking reference number and a confirmation message.
- A CTA button is shown which allows the user to view their bookings.

<details>
<summary>Confirmation page</summary>

![Screenshot of Confirmation page](/readme/confirmation.jpeg)
</details>


## 📜 Bookings
- The Bookings page shows a list of the user's bookings.
- An Edit button is shown for each booking which allows the user to edit the booking's passengers.
- The Booking detail page shows the booking's details and the passenger details.

<details>
<summary>Bookings page</summary>

![Screenshot of Bookings page](/readme/bookings.jpeg)
</details>

### ❌ Cancel Booking
- The user can cancel a booking by clicking the "Cancel Booking" button on the Booking detail page.
- This deletes the booking from the database by sending an AJAX request to the server and redirects the user to the Bookings page.
A confirmation dialog is shown to the user to confirm that they want to cancel the booking.

<details>
<summary>Cancel Booking</summary>

![Screenshot of Cancel Booking](/readme/cancel-booking.jpeg)
</details>


### 👥 Edit Passengers
- The user can edit a booking's passengers by clicking the "Edit Passengers" button on the Booking detail page.
- This sends an AJAX request (via htmx) to the server and loads the Passengers form with the booking's passenger data pre-populated.
- The user can then edit the passenger data and submit the form to update the booking's passenger data, or cancel the edit and return to the Booking detail page.

## 🌐 Blog
- The Blog is basic in design and is not a focus of this project.
- The Blog page shows a list of blog posts which were generated using the ChatGPT.
- The Blog detail page shows the blog post's title, image and content.
- New blog posts can be added via the Django Admin dashboard.

<details>
<summary>Blog page</summary>

![Screenshot of Blog page](/readme/blog.jpeg)
</details>

## 🤔 About
- The About page shows a brief description of the project and the technologies used.

<details>
<summary>About page</summary>

![Screenshot of About page](/readme/about.jpeg)
</details>

# 🛣️ Roadmap

<details>
<summary>Implement seat selection as per original design</summary>

![Screenshot of seat selection design](/readme/seat-selection.png)

</details>
<details>
<summary>Implement 'Extras' screen for seat selection, baggage selection, car hire and insurance as per original design.</summary>

![Screenshot of extras selection](/readme/extras-screen.png)

</details>
<details>
<summary>Build out flights page to show prices in alternate date selector, sort options, cart and edit search</summary>

![Search results screen](/readme/flight-results.png)

</details>
> Add password reset and "Remember me" login option 

---

# 🪲 Bugs

1. When styling the flight search result cards, there was some difficulty in adding a transition to animate the expansion of the card when clicked, to show the fares. It was found that it is not possible to transition from `display:hidden`, nor is it possible to transition from heigh:0 to height:auto. A workaround was implemented by setting `max-height:0` with `overflow:hidden` then using JavaScript to add `max-height:100rem` (or any other large value) along with `transition:all` to animate the card expansion and collapse.
2. The "alternate date selector" on the flight results page works by sending an AJAX request (via htmx) when an alternate date is clicked, and responding with HTML with the new flight data for the given date. When the new HTML is loaded from the response, the click event listeners need to be re-attached to the new flight card elements so that they expand when clicked, to show the fares. However, when initially trying to implement this re-attachment, an issue arose where the flight cards would not expand every second time an alternate date was selected. Following some troubleshooting, it was found that the click event listeners were compounding, thus negating each other (i.e. as if a user clicked the card twice in rapid succession). Using `console.log` and Chrome Dev Tools for debugging enabled me to see which events were firing so that the issue could be identified and solved by defining the click handler function outside of the event listner function. [Relevant Stack Overflow thread.](https://stackoverflow.com/questions/41720943/rebind-javascript-events-and-addeventlistener-fires-twice)
3. The `Flight`s table contains 90,000 rows of data and when implementing the `Booking`s CRUD functionality, there were severe issues experienced particularly in the admin panel when trying to view/edit `Booking`s which resulted in indefinite loading times as the `Flight`s data was loaded. Django has a number of built-in solutions for this issue and a solution was implemented by defining `search_fields` and `autocomplete_fields` in the `ModelAdmin` configurations for the `Flight` and `Booking` models. [Django Documentation Reference](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.autocomplete_fields)
4. When testing the site on mobile, a bug was identified where the date input field placeholder text would not display. Following some research and troubleshooting, it was found that this is a known issue with Flatpickr and a workaround was found as [referenced in this JSfiddle](https://jsfiddle.net/Sova12309/7bmpy9jc/9/).

<details>
<summary>Code Snippet Implemented</summary>

```css
.flatpickr-mobile:before {
  content: attr(placeholder);
  color: #9ca3af;
  width: 100%;
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

## ⚙️ Technologies Used

This section outlines the various technologies used throughout the project and the purpose each serves.

### 💾 Core Development Technologies

- [Django](https://www.djangoproject.com/) used as a full-stack framwork for developing the app.
- [JavaScript](https://www.ecma-international.org/publications-and-standards/standards/ecma-262/) used for client-side interaction and validation.
- [HTML](https://html.spec.whatwg.org/)/[CSS](https://www.w3.org/Style/CSS/Overview.en.html) + [Django Template Language](https://docs.djangoproject.com/en/4.2/ref/templates/language/) used for building out site pages.

### 📚 Libraries, Frameworks and Packages

- [Tailwind CSS](https://tailwindcss.com/) - used to style elements throughout the site.
- [Flowbite](https://htmx.org/) - a Tailwind-based open-source library; used very sparingly for small number of minor components in the site (radio select, dropdown select)
- [htmx](https://htmx.org/) - an open-source lightweight library used to fetch and load content dynamically via AJAX requests. Utilised specifically for fetching new `Flight` data and `Passenger`s edit form.
- [Flatpickr](https://flatpickr.js.org/) - a JavaScript library which provides the date picker styles and functionality on the Homepage.
- [Payform](https://github.com/jondavidjohn/payform) - a JavaScript library used for formatting the Payment Details form inputs.

#### 🐍 Python/Django Packages

- [Gunicorn](https://pypi.org/project/gunicorn/) - provides HTTP server.
- [psycopg2](https://pypi.org/project/psycopg2/) - provides PostgreSQL connection.
- [Pillow](https://pypi.org/project/Pillow/) - used for image processing (Model ImageField).
- [Whitenoise](https://pypi.org/project/whitenoise/) - used for serving static files.
- [Coverage](https://pypi.org/project/coverage/) - used for testing and analysis.
- [Django Markdown Field](https://pypi.org/project/django-markdownfield/) - adds a markdown-compatible text field to admin panel (for BlogPost model).
- [Black](https://pypi.org/project/black/) - A PEP8 compliant code formatter.
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) - used for debugging.

### 🖥️ Infrastructural Technologies

- [PostgreSQL](https://www.postgresql.org/) (via Digital Ocean) - used for database.
- [Heroku](https://www.heroku.com/) - used for hosting the application.

---

# 🧪 Testing

## 🤖 Automatic Testing

- Automated unit tests were written for core back-end functionality of the app to test data validation and integrity, templates used, HTTP status codes, user input etc.
- 35 tests were written in total.
- The [`Coverage`](https://pypi.org/project/coverage/) package was used to assist in guiding test requirements.
- 100% coverage was achieved on the `core` models and views.
- Future plans to write unit tests for coverage on `blog` and `users` apps.

<detail>
<summary>Test coverage report</summary>

![Coverage report](/readme/test-coverage.png)

</detail>

## ⚒️ Manual Testing

### 🛰️ Overview

- Responsiveness was tested as per below table (go to section: [Responsiveness](#responsiveness))
- All HTML files were passed through the W3C validator with no errors
- All JavaScript files were passed through JSHint with no errors present.
- The website was tested on major browsers including Chrome, Safari, Firefox and Edge as detailed in [Testing Process](#testing-process) below.
- All user flows were tested in depth including navigating through the booking flow, viewing blog content, entering search queries, clicking CTAs and links, and form submission.
- All forms were tested to ensure validation was present and that forms could be submitted without error
- Lighthouse was used to test for Performance, Accessibility, Best Practices and SEO and adjustments were made to improve test results.

---

### 🧪 General Testing
<details>
<summary>Expand test detail</summary>

| Test                  | Action                                                                                                                                                                                         | Success Criteria                                                              |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Homepage loads        | Navigate to website URL                                                                                                                                                                        | Page loads < 3s, no errors                                                    |
| Links                 | Click on each Navigation link, CTA, button, logo, footer link                                                                                                                                  | Correct page is loaded/correct action performed, new tab opened if applicable |
| Form validation       | Enter data into each input field, ensure only valid data is accepted                                                                                                                           | Form doesn't submit until correct data entered, error message shown           |
| Responsiveness        | Resize viewport window from 320px upwards with Chrome Dev Tools. Test devices as detailed in [Testing Process](#testing-process)                                                               | Page layout remains intact and adapts to screen size as intended              |
| Lighthouse            | Perform Lighthouse test on each page for the primary user flow (Booking process)                                                                                                                                                           | Score of > 89 on Performance, Accessibility, Best Practices              |
| Browser compatibility | Test links, layout, appearance, functionality and above Tests on Chrome, Safari, Firefox and Edge. BrowserStack used to test various mobile/large format devices with recent browser versions. | Website looks and functions as intended and passes all tests above            |

</details>

---

### 🏠 Homepage & Search Testing

<details>
<summary>Expand test detail</summary>

| Test                         | Action                                                                                                             | Success Criteria                                                                                                                                                                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Origin/Destination selection | - Click Origin/Destination fields.                                                                                 | - Drop down menu opens with correct data.<br>- Text input disabled. <br>- Dropdown closes on click outside. <br>- Correct selection added to field.                                                                                         |
| Trip type selection          | - Select trip type (return/one-way)                                                                                | - One-way trip hides return date field. <br>- Return trip shows return date field.                                                                                                                                                          |
| Date selection               | - Click date field                                                                                                 | - On click, show date picker.<br>- Dates in the past disabled.<br>- Dates after 01-07-2024 disabled.<br>- Correct selection added to field.                                                                                                 |
| Passenger selection          | - Click passengers field                                                                                           | - Drop down menu displays with up to 8 passengers                                                                                                                                                                                           |
| Form submission              | - Fill in form and click submit button                                                                             | - Form submitted<br>- Flight results page loaded with correct data                                                                                                                                                                          |
| Validation                   | - Select same origin and destination<br>- Select return date before selected outbound date<br>- Leave fields blank | - Field validation message shown if same origin and destination<br>- Field validation message shown if return date before outbound date<br>- Field validation messages shown for blank fields<br>- Form does not submit until data is valid |
</details>

---

### ✈️ Flight Search Results Testing
<details>
<summary>Expand test detail</summary>

| Test            | Action                                               | Success Criteria                                                                                                           |
| --------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Flight results  | - Review flight results                              | - Correct flight data shown                                                                                                |
| Alternate dates | - Select alternate dates for outbound/return flights | - Correct flight data fetched<br>- Correct dates added to selector<br>- Error message shown if same/invalid dates selected |
| Fare selection  | - Select a fare                                      | - Fares container expands on click<br>- Correct fare data shown<br>- Fare/flight selection works as intended               |
| Edit flight     | - Edit a flight selection                            | - When edit button clicked, flight results show and new flight can be selected                                             |
| Confirm flights | - Select flights and confirm                         | - When confirmed, date added to session storage and request sent                                                           |

</details>

---

### 💵 Payment & Confirmation Testing
<details>
<summary>Expand test detail</summary>

| Test            | Action                                               | Success Criteria                                                                                                           |
| --------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Flight results  | - Review flight results                              | - Correct flight data shown                                                                                                |
| Alternate dates | - Select alternate dates for outbound/return flights | - Correct flight data fetched<br>- Correct dates added to selector<br>- Error message shown if same/invalid dates selected |
| Fare selection  | - Select a fare                                      | - Fares container expands on click<br>- Correct fare data shown<br>- Fare/flight selection works as intended               |
| Edit flight     | - Edit a flight selection                            | - When edit button clicked, flight results show and new flight can be selected                                             |
| Confirm flights | - Select flights and confirm                         | - When confirmed, date added to session storage and request sent                                                           |
</details>

---

### 🔒 Authorisation Testing
<details>
<summary>Expand test detail</summary>

| Test            | Action                                               | Success Criteria                                                                                                           |
|-----------------|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Flight results  | - Review flight results                              | - Correct flight data shown                                                                                                |
| Alternate dates | - Select alternate dates for outbound/return flights | - Correct flight data fetched<br>- Correct dates added to selector<br>- Error message shown if same/invalid dates selected |
| Fare selection  | - Select a fare                                      | - Fares container expands on click<br>- Correct fare data shown<br>- Fare/flight selection works as intended               |
| Edit flight     | - Edit a flight selection                            | - When edit button clicked, flight results show and new flight can be selected                                             |
| Confirm flights | - Select flights and confirm                         | - When confirmed, date added to session storage and request sent                                                           |                                       |
</details>

---

### 🚦 Lighthouse Testing
- All pages were tested using Lighthouse with the primary goals of identifying performance and accessibility issues and ensuring adherance to best practices. 
- The Lighthouse test results for each step of the `core` user flow are shown below:
<details>
<summary>Homepage</summary>

![Homepage Lighthouse test](/readme/Lighthouse-homepage.png)
</details>
<details>
<summary>Flights</summary>

![Flights Lighthouse test](/readme/Lighthouse-flights.png)
</details>
<details>
<summary>Passengers</summary>

![Passengers Lighthouse test](/readme/Lighthouse-passengers.png)
</details>
<details>
<summary>Checkout</summary>

![Checkout Lighthouse test](/readme/Lighthouse-summary.png)
</details>
<details>
<summary>Bookings Overview</summary>

![Bookings Lighthouse test](/readme/Lighthouse-bookings.png)
</details>
<details>
<summary>Booking Detail</summary>

![Booking Detail Lighthouse test](/readme/Lighthouse-booking-detail.png)
</details>


---

# 👋 Credits

- [Unsplash](https://unsplash.com/) - used for sourcing Blog photographic images.
- [ChatGPT](https://openai.com/chatgpt) - used for generating all Blog text content.
- [Favicon.io](https://favicon.io/) - used to create favicon.
- [Payform](https://github.com/jondavidjohn/payform) - used for Payment Details input formatting.
- [Mockaroo](https://www.mockaroo.com/) - used for creating model data.
