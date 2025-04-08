# NeedleDrop

NeedleDrop is a Django we application inspire by [Discogs](https://discogs.com). It allows users to catalog their personal music collection - from vinyl records to CDs and digital releases - while exploring releases by artists, track their ownership details, and managing their own curated archive.

---

## Overview

NeedleDrop was created as a music collection manager that focuses on personal library organization. Users can add artists and releases, and associate those releases with their own collections, including condition, notes, and sales status.

---

## Features

- Full CRUD for:
    - Artist
    - Releases
    - User collection entries
- User authentication
- Only the user who owns a collection entry can edit or delete it
- Pre-filled edit forms
- Responsive layout and UI

---

## User Stories

- AAU, I want to create an account so I can manage my personal music collection.
- AAU, I want to log in and out securely so my collection data stays private.
- AAU, I want to browse a list of all artists and releases in the database.
- AAU, I want to add a new artist and release if it's not already in the system.
- AAU, I want to add a release to my personal collection and specify the condition, ownership date, and any notes.
- AAU, I want to see a list of all the music releases I own.
- AAU, I want to edit the details of a release in my collection.
- AAU, I want to delete a release from my collection if i no longer own it.
- AAU, I want to search or filter my collection by artist, format, or condition.
- AAU, I want to mark items in my collection as "for sale."
- AAU, I want to view detailed information about a specific artist or release.
- AAU, I want to see a consistent, visually appealing layout across the app.

---

## Technologies Used

- Scheduling & Task Organization:
    - Trello
    - ChatGPT 4o

- Design:
    - Figma

- Development:
    - Python 3
    - Django
    - PostgreSQL
    - HTML 5
    - CSS

- Deployment:
    - Heroku

---

## Data Model Breakdown

### User - 1:N

- [PK] userId
- username: CharField
- password: CharField
- First Name: CharField
- Last Name: CharField

### Artist - 1:N

- name: CharField
- genre: CharField
- bio: TextField (optional)

### Release - 1:N

- title: CharField
- artist: ForeignKey -> Artist
- release_date: DateField
- label: CharField
- format: ChoiceField (Vinyl, CD, Cassette, etc.)
- cover_image: URL or FileField
- description: TextField (optional)

### Review - 1:N

- user: ForeignKey -> User
- release: ForeignKey -> Release
- rating: PositiveIntegerField (1-5)
- review_text: TextField (optional)
- created_at: DateTimeField 

### CollectionEntry - N:N

- user: ForeignKey -> User
- release: ForeignKey -> Release
- condition: ChoiceField (New, Mint, Very Good, etc.)
- owned_since: DateField
- notes: DateField
- is_for_sale: BooleanField

### WishListItem - N:N

- user: ForeignKey -> User
- release: ForeignKey -> Release
- priority: ChoiceField (High, Medium, Low)
- note: TextField (optional)
- added_at: DatTimeField

---

## Development Guide & Pseudocode

### Notes:
- All work will be done on a `dev` branch.
- Merges to `main` will be committed after testing each specific functionality.
- Final merge to `main` will occur prior to project submission and presentation.

### 0. Web Design Planning (Figma)
- [ ] Create a new Figma project: "NeedleDrop UI"
- [ ] Define the visual theme (colors, fonts, spacing, branding)
- [ ] Sketch a wireframe for each major page:
  - [ ] Home / Landing page
  - [ ] Login/Register
  - [ ] Release List & Detail Page
  - [ ] Collection Dashboard
  - [ ] Wishlist Page
  - [ ] Review Section / Form
- [ ] Use Frames to define layout using Flexbox-style or grid layout
- [ ] Label all components: buttons, navbars, cards, inputs, etc.
- [ ] Group reusable UI elements (e.g. release cards, review blocks)
- [ ] Define color palette and check accessibility contrast
- [ ] Export or screenshot key screens for use in documentation
- [ ] (Optional) Share Figma link in README for visual reference

### 1. Project & Git Setup
- [ ] Create GitHub repo: `needledrop`
- [ ] Clone locally
- [ ] Create and switch to `dev` branch
- [ ] Initialize Django project: `django-admin startproject needledrop`
- [ ] Create app: `python manage.py startapp collection`
- [ ] Install psycopg2 and create PostgreSQL DB
- [ ] Connect PostgreSQL in `settings.py`
- [ ] Run `migrate` and create superuser

### 2. Models & Relationships
- [ ] Define models:
  - [ ] Artist: name, genre, bio
  - [ ] Release: title, FK to Artist, format, release_date, cover_image, description
  - [ ] CollectionEntry: FK to User + Release, condition, owned_since, notes, is_for_sale
  - [ ] WishListItem: FK to User + Release, priority, note, added_at
  - [ ] Review: FK to User + Release, rating, review_text, created_at
- [ ] Run `makemigrations` and `migrate`
- [ ] Register all models in `admin.py`

### 3. Authentication
- [ ] Enable login, logout, and register functionality
- [ ] Create views/templates for authentication
- [ ] Use `@login_required` on collection, wishlist, review views
- [ ] Use `{% if request.user.is_authenticated %}` to control access in templates

### 4. Templates & Base Layout
- [ ] Create `base.html` with nav links:
  - Home | My Collection | My Wishlist | My Reviews | Login | Logout
- [ ] Use `{% block content %}` and extend `base.html` in all views
- [ ] Create templates for:
  - [ ] Artist list/detail
  - [ ] Release list/detail

### 5. CollectionEntry CRUD
- [ ] Create view to list user's collection entries
- [ ] Create form to add a release to user's collection
- [ ] Create form to edit collection details (condition, notes, for sale)
- [ ] Create view to delete collection entry
- [ ] Restrict edit/delete buttons to `entry.user == request.user`

### 6. WishListItem CRUD
- [ ] Create wishlist view for current user
- [ ] Create form to add release to wishlist (with priority and note)
- [ ] Create option to remove from wishlist
- [ ] Prevent duplicate wishlist entries (enforce `unique_together`)
- [ ] Add "Add to Wishlist" button to release detail page

### 7. Review CRUD
- [ ] Create review form (rating and optional text)
- [ ] Show user's review on release detail page
- [ ] Prevent multiple reviews per user per release (unique constraint)
- [ ] Create views to edit and delete reviews
- [ ] Display average rating on each release detail page

### 8. Unit Tests
- [ ] Create `tests.py` file
- [ ] Write model tests for Review:
  - [ ] Creation
  - [ ] Uniqueness
  - [ ] Rating value
- [ ] Write model tests for WishListItem:
  - [ ] Creation
  - [ ] Default priority
  - [ ] Uniqueness
- [ ] Run tests with `python manage.py test`

### 9. Final Polish
- [ ] Ensure consistent template layout across pages
- [ ] Add alt text for all cover images
- [ ] Style all buttons and forms using CSS Grid/Flexbox
- [ ] Ensure text contrast meets accessibility standards (WCAG AA)
- [ ] Remove unused or commented-out code

### 10. Deployment & Submission
- [ ] Set up production config for Render/Railway
- [ ] Configure `ALLOWED_HOSTS` and collect static files
- [ ] Deploy app to hosting platform
- [ ] Finalize `README.md`:
  - [ ] Screenshot
  - [ ] Live app link
  - [ ] User stories
  - [ ] Technologies used
  - [ ] Development schedule
  - [ ] ERD diagram
- [ ] Merge `dev` branch into `main`
- [ ] Push final code and tag submission commit
- [ ] Submit repo and live link

### 11. Presentation Prep
- [ ] Prepare presentation walkthrough:
  - [ ] What the app does
  - [ ] How it works (models, views, templates)
  - [ ] Key features
  - [ ] Challenges you solved
  - [ ] What you'd add with more time

---

## Development Schedule for Trello

### April 8th (Tue) - Proposal & Setup
- Finalize project proposal and pitch
- Submit GitHub repo
- Create and switch to `dev` branch
- Finalize data model
- Scaffold Django project `needledrop` and structure for app `collection`
- Set up PostgreSQL in `setting.py`
- Create initial models:
    - `Artist`
    - `Release`
    - `CollectionEntry`
    - `Review`
    - `WishListItem`
    - Create ERD and add to `README.md`

### April 9th (Wed) - Auth, Core Models & Initial Deployment
- Implement user authentication (login/register/logout)
- Add login-required restrictions to protected views
- Build list/detail templates for Artists and Releases
- Register users in admin and test base permissions
- Set up `base.html` with nav links and template inheritance
- Initial deployment to Heroku

### April 10th (Thu) - CRUD: `CollectionEntry`
- Build collection views (list, create, update, delete)
- Tie entries to current user only
- Use Django forms with prefilled data for editing
- Add logic to only show edit/delete to entry owner
- Test form validation

### April 11th (Fri) - CRUD: `Reviews` & `WishListItems`
- Create `Review` form and views (add/edit/delete)
- Prevent duplicate reviews per user/release
- Create `WishListItem` views and templates
- Allow priority setting and optional note
- Add/remove wishlist buttons on release detail page

### April 12th (Sat) - Styling & Layout Polish
- Finalize `base.html` layout
- Apply Flexbox/Grid for layout consistency
- Ensure visual theme consistency
- Add contrast-compliant colors
- Style all buttons and forms
- Add `alt` text to all images

### April 13th (Sun) - User Views & Filtering
- Build user-specific dashboards:
  - My Collection
  - My Reviews
  - My Wishlist
- Add basic filters (by artist, format, etc.)
- (Stretch) Add review average/star visual
- Ensure public detail pages are accessible

### April 14th (Mon) - Unit Testing, Debugging, Deployment
- Write tests for:
  - Review: creation, unique constraint
  - WishListItem: default priority, uniqueness
- Run full test suite (`python manage.py test`)
- Debug all known issues
- Deploy app to Render or Railway
- Final polish of `README.md` (screenshot, links, stories)
- Final merge `dev` → `main`
- Tag commit for submission

### April 15th (Tue) - Submission & Presentation
- Submit GitHub repo + live app link
- Present to class:
  - What it does
  - How it works
  - Features you're proud of
  - Challenges you solved

---

### Stretch Goals

- Implement search and filter tools by artist, genre, or format
- Public user profiles and browsing others' collections
- Tagging system for releases
- Add cover art upload feature
- Marketplace integration and/or price tracking with Stripe

---

## Conclusion

NeedleDrop is a focused, user-first music cataloging app that demonstrates an understanding of Django's architecture, user authentication, and relational data modeling.