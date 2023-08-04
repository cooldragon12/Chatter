/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{html,js,ts,jsx,tsx}"],
  theme: {
    fontFamily: {
      sans:['Inter', 'sans-serif'],
    },
    extend: {
      colors: {
        'text': '#151104',
        'background': '#fdfbf7',
        'primary':{ 
          DEFAULT:'#183072',
          100:"#eaeefb",
          200:"#c0cdf2",
          300:"#96ace9",
          400:"#4269d7",
          500:"#2850bd",
          600:"#162c69",
          700:"#0d1b3f",
          dark:'#040915'
        },
        'secondary': '#cbc0f2',
        'accent': {
          DEFAULT:'#0B6179',
          100:'#e8f8fd',
          200:'#b9ebf8',
          300:'#8addf4',
          400:'#5cd0f0',
          500:'#2dc2eb',
          600:'#14a9d2',
          700:'#0f83a3',
          800:'#0b5e75',
          900:'#073846',
          dark:'#021317'
        },
      },
      backgroundSize: ({ theme }) => ({
        auto: 'auto',
        cover: 'cover',
        contain: 'contain',
        ...theme('spacing')
      }),
      width:{
        'whole':'calc(100vw - 4rem)',
      },
      height:{
        'whole':'calc(100vh - 4rem)',
      }

    },
  },
  plugins: [],
}

