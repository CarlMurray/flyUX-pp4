


# 📄 Project Background

![Cover image](/readme/cover-img.png)


### 👀 Overview

- This Django web development project is a continuation of a UX Design project I completed during my Diploma in UX Design with the UX Design Institute which goes through the full UX process from user research all the way through to prototyping and handover.
- The end result was a user-friendly flight booking flow which was informed by user research and prototyped to a medium fidelity in Figma.
- Revisiting the project a year later, I am now using it as a foundation to build upon and bring it from Figma prototype, to a fully functioning Django-based full-stack web application, combining my passions for user-centric design and web development to build a holistic solution.

**[See here for the full UX Design case study](https://carlmurray.design/p/cmurray/03678e7f)**

# 🔁 Process

### ❓ Problem Statement:

> Your client is a start-up airline. They’re looking to create an online experience that is fast, easy and intuitive: one that’s based on a deep understanding of their target users.

### 🔎 Research

<details>

- Competitive benchmarking was carried out to better understand what current industry leaders are doing and to understand common conventions and user expectations from a flight booking flow.
- Usability testing of existing flows were carried out with users on the Aer Lingus, Ryanair and EasyJet websites to observe user behaviour, mental models, positives and pain points.
- This research data was used to inform my solution, which aimed to provide a simple, straight-forward, upsell-free and easy-to-use flight booking flow.

**[See here for the full UX Design case study](https://carlmurray.design/p/cmurray/03678e7f)**

</details>

### 🎨 Design

<details>

- The design process began with sketching out low-fidelity wireframes to explore different layout options and to get a feel for the flow.
- The wireframes were then translated into a [medium-fidelity prototype](https://www.figma.com/proto/1lcdpwiJdrfa5DN0flygbf/Project10?type=design&node-id=2-3&t=7HxbLkrQd03aCuJy-1&scaling=scale-down&page-id=0%3A1&starting-point-node-id=2%3A3&show-proto-sidebar=1&mode=design) in Figma.
- Handover documentation was created to provide a detailed overview of the design and to provide guidance for the development process.
- The design was informed by the research data and aimed to provide a simple, straight-forward, upsell-free and easy-to-use flight booking flow.
- Branding was kept minimal and the design was kept clean and simple to allow for easy navigation and to avoid overwhelming the user with too much information.
- The logo, typeface and colour scheme were chosen to reflect the brand's values of simplicity, speed and efficiency.

![Colour palette](/readme/palette.png)

**[See here for the full UX Design case study](https://carlmurray.design/p/cmurray/03678e7f)**

</details>

### 👨‍💻 Development

<details>

- The development process was carried out using an Agile methodology with a focus on iterative development and continuous improvement.
- The project was managed using a GitHub Project board with user stories and tasks.
- User Stories were sized using T-shirt sizing (XS, S, M, L, XL) and prioritised based on the MoSCoW method (Must have, Should have, Could have, Won't have).

#### 📈 [Link to the GitHub Project board](https://github.com/users/CarlMurray/projects/3/views/3)

#### 👤 User Stories
1. As a user, I want to search for flights based on the selected departure airport, destination airport, and date, so that I can view the available flight options.
2. As a user, I want to see a list of available flights after performing a search, including relevant details such as flight number, departure time, arrival time, and price, so that I can choose a suitable flight.
3. As a user, I want to checkout quickly and securely on the site, so that I can finalise my booking.
4. As a user, I want to provide my personal information (e.g. name, email, phone number) during the booking process, so that I can receive information about the flight.
5. As a user, I want to review the booking details before finalising the booking, so that I can ensure everything is correct.
6. As a user, I want to confirm the booking and receive a confirmation message or email, so that I know my flight has been successfully booked.
7. As an admin, I want to view and update the details of a specific flight booking, including passenger information and booking status, so that I can handle customer inquiries and make necessary changes.
8. As an admin, I want to manage user accounts, including creating, editing, and disabling user profiles, so that I can maintain control over site access and user privileges.
9. As an admin, I want to log in to an admin panel securely, so that I can access the site's administrative features.
10. As an admin, I want to manage the list of flights, including adding, editing, and deleting flight details, so that I can update flight schedules and availability.
11. As an admin, I want to manage the list of airports, including adding, editing, and deleting airport entries, so that I can ensure accurate and up-to-date information.
12. As a user, I want to create an account so that I can keep track of and edit my existing bookings.
13. As a user I want to explore blog posts to get travel inspiration for my next trip.

</details>

<br>

--- 

### 🧮 Data Models

<details>

The data models for the project are shown below:

![Database schema](/readme/dbdiagram.png)

- Users app:
  - `User` - custom user model which extends the Django `AbstractUser` model. Default username field is replaced with email field.

<br>

- Core app:
  - `Flight` - represents a flight. Contains origin, destination, outbound date, flight number, aircraft, departure time, arrival time and price.
  - `Booking` - represents a booking. Contains user, trip email, flight(s), fare(s), booking reference number, booking date, total price and status.
  - `Passenger` - represents Passengers associated with a Booking. Contains first name, last name and Booking id.
  - `Airport` - represents an airport. Contains name, IATA code, locality, region and country.
  - `Aircraft` - represents aircraft flow for a given flight. Contains aircraft model/type, identification and number of seats. Note: The Aircraft model was originally implemented with the intention of using it to implement seat selection functionality and options for seating and fares configurations. However, this was not implemented due to time constraints and potential for scope creep.

<br>

- Blog app:
  - `BlogPost` - represents a blog post. Contains title, image, content, date created and content rendered which is required to render content created with a Markdown field. The Markdown field was added to the admin panel to allow for content formatting/styling.

<br>

</details>

---

<br>
<br>
<br>

---

# 🪀 Features

### 💩 CRUD Functionality

<details>

- User CRUD functionality is primarily related to `Booking`s.
  - Create: Users create a Booking by going through the full user flow. A `Booking` is created once the user completes checkout.
  - Read: Users can view their created `Booking`s and relevant `Booking` details when logged in.
  - Update: Users can edit a `Booking` by changing `Passenger` information for that `Booking`.
  - Delete: Users can cancel a `Booking` which deletes it from the database.
- Admin CRUD functionality exists for all Models and is done from the Django Admin dashboard.

</details>

### 🔑 Authentication & Authorisation

<details>

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
</details>

### 🧭 Navigation

<details>

- Primary navigation is located in the header and is present on all pages.
- A hamburger menu is present on mobile devices and expands to show the primary navigation links.

<details>
<summary>Navigation on homepage</summary>

![Screenshot of homepage ](/readme/homepage.jpeg)

</details>
</details>

### 🔎 Search

<details>

- The search form is located on the homepage and allows users to search for flights by entering their origin, destination, trip type, dates and number of passengers.
- The search form is validated on the front-end and back-end to ensure that the data entered is valid and that the search can be performed.
- If the search is valid, the user is redirected to the Flights page where they can view the search results.
- If the search is invalid, an error message is shown.

<details>
<summary>Homepage with search form</summary>

![Screenshot of homepage](/readme/homepage.jpeg)

</details>
</details>

### ✈️ Flights

<details>

- The Flights page shows the search results for the user's search query.
- If there are no results, an info message is shown prompting the user to try an alternate date.
- If there are results, the results are shown in a card format with the outbound and return flights shown in separate cards.
- Once flights have been selected, the CTA button is enabled and the user can proceed to the next step in the booking flow. Selected flight numbers are stored in session storage and are used to populate the Order Summary page.
<details>
<summary>Flights</summary>

![Screenshot of Flights page](/readme/flights.jpeg)

</details>
</details>

#### 🗓️ Alternate Dates

<details>

- The alternate dates feature allows users to view flight results for alternate dates to their original search query.
- The feature works by sending an AJAX request (via htmx) to the server with the new date, and the server responds with the new flight data for that date, and new date options for the alternate date selector.
- The new flight data is then loaded into the page and the click event listeners are re-attached to the new flight cards so that they expand when clicked, to show the fares.
- It is not possible to select a date that is in the past.
- It is not possible to select a date that is before the outbound date if the trip type is return.

</details>

#### 💸 Fares

<details>

- The fares are shown in a card format with the outbound and return fares shown in separate cards.
- The user can click on a fare card to expand it and show the fare details.
- The user can select a fare by clicking the button on the fare card.
- Selected fare information is stored in session storage and is used to populate the Order Summary page.

<details>
<summary>Fares</summary>

![Screenshot of Fares](/readme/flights-fares.jpeg)

</details>
</details>

#### 🛫 Edit Flights

<details>

- The user can edit their flight selection by clicking the "Edit" button on the fare card.
- This reloads the previous flight search results and allows the user to select new flights.

<details>
<summary>Edit Flights</summary>

![Screenshot of Edit Flights](/readme/flights-fares.jpeg)

</details>
</details>

### 👯 Passengers

<details>

- The Passengers form is shown after the user has selected their flights.
- The form is pre-populated with the number of passengers selected in the search form.
- If logged in, the form is pre-populated with the user's details.
- The "Confirm email" field is not pre-populated and must be entered by the user as a security and error prevention measure.

<details>
<summary>Passengers form</summary>

![Screenshot of Passengers form](/readme/passengers.jpeg)

</details>
</details>

### 💳 Checkout

<details>

- The Checkout page shows the Order Summary and the Payment Details form.
- The Order Summary is populated with the flight and fare information stored in session storage.
- For the purposes of this project, the Payment Details form is a mockup and does not process any payments. The form is lightly validated on the front-end using the Payform library with some minor modification to allow for dummy card data to be entered.

<details>
<summary>Checkout page</summary>

![Screenshot of Checkout page](/readme/checkout.jpeg)

</details>
</details>

### ✅ Confirmation

<details>

- The Confirmation page shows the user's booking reference number and a confirmation message.
- A CTA button is shown which allows the user to view their bookings.

<details>
<summary>Confirmation page</summary>

![Screenshot of Confirmation page](/readme/confirmation.jpeg)

</details>
</details>

### 📜 Bookings

<details>

- The Bookings page shows a list of the user's bookings.
- An Edit button is shown for each booking which allows the user to edit the booking's passengers.
- The Booking detail page shows the booking's details and the passenger details.

<details>
<summary>Bookings page</summary>

![Screenshot of Bookings page](/readme/bookings.jpeg)

</details>
</details>

#### ❌ Cancel Booking

<details>

- The user can cancel a booking by clicking the "Cancel Booking" button on the Booking detail page.
- This deletes the booking from the database by sending an AJAX request to the server and redirects the user to the Bookings page.
  A confirmation dialog is shown to the user to confirm that they want to cancel the booking.

<details>
<summary>Cancel Booking</summary>

![Screenshot of Cancel Booking](/readme/cancel-booking.jpeg)

</details>
</details>

#### 👥 Edit Passengers

<details>

- The user can edit a booking's passengers by clicking the "Edit Passengers" button on the Booking detail page.
- This sends an AJAX request (via htmx) to the server and loads the Passengers form with the booking's passenger data pre-populated.
- The user can then edit the passenger data and submit the form to update the booking's passenger data, or cancel the edit and return to the Booking detail page.

</details>

### 🌐 Blog

<details>

- The Blog is basic in design and is not a focus of this project.
- The Blog page shows a list of blog posts which were generated using the ChatGPT.
- The Blog detail page shows the blog post's title, image and content.
- New blog posts can be added via the Django Admin dashboard.

<details>
<summary>Blog page</summary>

![Screenshot of Blog page](/readme/blog.jpeg)

</details>
</details>

### 🤔 About

<details>

- The About page shows a brief description of the project and the technologies used.

<details>
<summary>About page</summary>

![Screenshot of About page](/readme/about.jpeg)

</details>
</details>

---

<br>
<br>
<br>

# 🛣️ Roadmap

<details>

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

</details>

---

<br>
<br>
<br>

# 🪲 Bugs

<details>

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

<br>

  5. When testing the alternate date selection feature, a bug was identified where the "No flights on selected date" error message would not disappear during the transition between a newly selected alternate date. Additionally, if the fares container was expanded for a flight, it would remain visible during the request when selecting a new date. The loading indicator would display during the request, but would push the error message/fares container down. The intended behaviour was for all content - including flights, fares and error messages - to be hidden during a request, and for the loading indicator to display. Some time was spent troubleshooting the `htmx` implementation, however it was found that all that needed to be done was add `classList.add('hidden')` to these elements when an alternate date was clicked, as I had done for the flight cards already in the earlier stages of development. This was a simple fix and a reminder to always ensure code is clean and well documented, as I had already forgotten how I had implemented this functionality on the flight cards by the time I was reaching the latter stages of development.

<details>
<summary>Screenshot of bug</summary>

![Screenshot of bug](/readme/no-flights-bug.png)

</details>

</details>

---

<br>
<br>
<br>

# ⚙️ Technologies Used

This section outlines the various technologies used throughout the project and the purpose each serves.

## 💾 Core Development Technologies

<details>

- [Django](https://www.djangoproject.com/) used as a full-stack framwork for developing the app.
- [JavaScript](https://www.ecma-international.org/publications-and-standards/standards/ecma-262/) used for client-side interaction and validation.
- [HTML](https://html.spec.whatwg.org/)/[CSS](https://www.w3.org/Style/CSS/Overview.en.html) + [Django Template Language](https://docs.djangoproject.com/en/4.2/ref/templates/language/) used for building out site pages.

</details>

## 📚 Libraries, Frameworks and Packages

<details>

- [Tailwind CSS](https://tailwindcss.com/) - used to style elements throughout the site.
- [Flowbite](https://htmx.org/) - a Tailwind-based open-source library; used very sparingly for small number of minor components in the site (radio select, dropdown select)
- [htmx](https://htmx.org/) - an open-source lightweight library used to fetch and load content dynamically via AJAX requests. Utilised specifically for fetching new `Flight` data and `Passenger`s edit form.
- [Flatpickr](https://flatpickr.js.org/) - a JavaScript library which provides the date picker styles and functionality on the Homepage.
- [Payform](https://github.com/jondavidjohn/payform) - a JavaScript library used for formatting the Payment Details form inputs.

</details>

## 🐍 Python/Django Packages

<details>

- [Gunicorn](https://pypi.org/project/gunicorn/) - provides HTTP server.
- [psycopg2](https://pypi.org/project/psycopg2/) - provides PostgreSQL connection.
- [Pillow](https://pypi.org/project/Pillow/) - used for image processing (Model ImageField).
- [Whitenoise](https://pypi.org/project/whitenoise/) - used for serving static files.
- [Coverage](https://pypi.org/project/coverage/) - used for testing and analysis.
- [Django Markdown Field](https://pypi.org/project/django-markdownfield/) - adds a markdown-compatible text field to admin panel (for BlogPost model).
- [Black](https://pypi.org/project/black/) - A PEP8 compliant code formatter.
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) - used for debugging.

</details>

## 🖥️ Infrastructural Technologies

<details>

- [PostgreSQL](https://www.postgresql.org/) (via Digital Ocean) - used for database.
- [Heroku](https://www.heroku.com/) - used for hosting the application.

</details>

</details>

---

<br>
<br>
<br>

# 🧪 Testing

## 🤖 Automatic Testing

<details>

- Automated unit tests were written for core back-end functionality of the app to test data validation and integrity, templates used, HTTP status codes, user input etc.
- 35 tests were written in total.
- The [`Coverage`](https://pypi.org/project/coverage/) package was used to assist in guiding test requirements.
- 100% coverage was achieved on the `core` models and views.
- Future plans to write unit tests for coverage on `blog` and `users` apps.

<details>
<summary>Test coverage report</summary>

![Coverage report](/readme/test-coverage.png)

</details>
</details>

## ⚒️ Manual Testing

### 🛰️ Overview

<details>

- Responsiveness was tested as per below table (go to section: [Responsiveness](#responsiveness))
- All HTML files were passed through the W3C validator with no errors
- All JavaScript files were passed through JSHint with no errors present.
- The website was tested on major browsers including Chrome, Safari, Firefox and Edge as detailed in [Testing Process](#testing-process) below.
- All user flows were tested in depth including navigating through the booking flow, viewing blog content, entering search queries, clicking CTAs and links, and form submission.
- All forms were tested to ensure validation was present and that forms could be submitted without error
- Lighthouse was used to test for Performance, Accessibility, Best Practices and SEO and adjustments were made to improve test results.

</details>

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
| Lighthouse            | Perform Lighthouse test on each page for the primary user flow (Booking process)                                                                                                               | Score of > 89 on Performance, Accessibility, Best Practices                   |
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
| --------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | --- |
| Flight results  | - Review flight results                              | - Correct flight data shown                                                                                                |
| Alternate dates | - Select alternate dates for outbound/return flights | - Correct flight data fetched<br>- Correct dates added to selector<br>- Error message shown if same/invalid dates selected |
| Fare selection  | - Select a fare                                      | - Fares container expands on click<br>- Correct fare data shown<br>- Fare/flight selection works as intended               |
| Edit flight     | - Edit a flight selection                            | - When edit button clicked, flight results show and new flight can be selected                                             |
| Confirm flights | - Select flights and confirm                         | - When confirmed, date added to session storage and request sent                                                           |     |

</details>

---

### 🚦 Lighthouse Testing

<details>

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
</details>

---

### 📱 Responsiveness Testing

<details>

- Testing for responsiveness was conducted using Chrome Dev Tools and ResponsivelyApp.
- The website was tested extensively on a range of emulated mobile, tablet and large format screen sizes in both portrait and landscape orientations.
<details>
<summary>Responsiveness test results</summary>

![Responsiveness testing with ResponsivelyApp](/readme/responsive-testing.png)

</details>

| Device             | iPhone SE   | iPhone X    | iPhone 12 Pro | iPhone 13 Pro Max | iPhone 14 Pro Max | iPad         | iPad Air     | iPad Pro      | Macbook Pro  |
| ------------------ | ----------- | ----------- | ------------- | ----------------- | ----------------- | ------------ | ------------ | ------------- | ------------ |
| **Resolution**     | **375x667** | **375x812** | **390x844**   | **414x76**        | **414x896**       | **768x1024** | **820x1180** | **1024x1366** | **1440x900** |
| Render             | Pass        | Pass        | Pass          | Pass              | Pass              | Pass         | Pass         | Pass          | Pass         |
| Layout             | Pass        | Pass        | Pass          | Pass              | Pass              | Pass         | Pass         | Pass          | Pass         |
| Functionality      | Pass        | Pass        | Pass          | Pass              | Pass              | Pass         | Pass         | Pass          | Pass         |
| Links              | Pass        | Pass        | Pass          | Pass              | Pass              | Pass         | Pass         | Pass          | Pass         |
| Images             | Pass        | Pass        | Pass          | Pass              | Pass              | Pass         | Pass         | Pass          | Pass         |
| Portrait/Landscape | Pass        | Pass        | Pass          | Pass              | Pass              | Pass         | Pass         | Pass          | Pass         |

</details>

---

<br>
<br>
<br>

# 👋 Credits

<details>

- [Unsplash](https://unsplash.com/) - used for sourcing Blog photographic images.
- [ChatGPT](https://openai.com/chatgpt) - used for generating all Blog text content.
- [Favicon.io](https://favicon.io/) - used to create favicon.
- [Payform](https://github.com/jondavidjohn/payform) - used for Payment Details input formatting.
- [Mockaroo](https://www.mockaroo.com/) - used for creating model data.

</details>
