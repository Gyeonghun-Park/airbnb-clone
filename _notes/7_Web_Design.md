# 7. Web Design

## 19 Intro to Tailwind CSS

### What is Gulp?

- SCSS -> ugly CSS
- New JavaScript -> Old JavaScript
- Pug.js -> ugly HTML
- uploading to github automization

we do not utilize babel nor yarn for this project

```shell
npm init
npm install gulp gulp-postcss gulp-sass gulp-csso node-sass auto-prefixer -D
npm install tailwindcss -D
```

- If you don't do npm init, then node modules will be installed in upper directory with npm on it
- initialize tailwind css

```shell
npx tailwindcss init
```

### Compile scss to css

- make alias on package.json

  ```json
  "scripts": {
      "css": "gulp"
    }
  ```

- compile scss into css file

  ```shell
  npm run css
  ```

### Integrating css to HTML

- static path: http://127.0.0.1:8000/static/css/styles.css

- loading static path to html: replacing http://127.0.0.1:8000/static to tag {static}

  ```html
  {% load static %} <link rel="stylesheet" href="{% static "css/styles.css" %}">
  ```

- CSS is already done by tailwind css at styles.css

- Call tailwind css by using class="tailwind-css-classname"
  [Refer tailwind css document for classnames](https://tailwindcss.com/docs/border-color)

- em is relative to closest font-size

- rem is relative to root font size

## 20 Design

### [Cloning Airbnb login](./templates/users/login.html)

- Example page for Cloning

  ![image-20200316212523408](_img/airbnb_login.png)
