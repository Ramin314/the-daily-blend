/** @type {import('tailwindcss').Config} */
module.exports = {
  purge:[
    './templates/**/*.html',
  ],
  content: [
    'node_modules/preline/dist/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('preline/plugin'),
  ],
}

