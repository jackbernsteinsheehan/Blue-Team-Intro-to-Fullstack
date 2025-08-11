
# Frontend start HERE! # 

Please read the overview file /README.md if you haven't yet.

As mentioned in this file, we will be using our Next.js framework that will allow us to start to design and create the entire application that will connect to the functions on the backend via API.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

Firstly, we will need to ensure we have the Node.js runtime that comes with npm (node package manager)

Find out how to install Node.js. To enure the installation was successful, you should be able to run the two commands:
```bash
node -v
npm -v
```

Assuming you are located at the root of the project you should **always** be located at the `frontend/` directory for any testing and package installations. To do so, just do `cd frontend` on your terminal.

Now install Next.js: https://nextjs.org/docs/app/getting-started/installation
Follow the simple few installation instructions and perhaps read a little bit of how Next.js works.

When you run the main command a bunch of options will come out and you will be prompted to select. For this, just say "yes" to everything as a way to set everything to its default values. And in the end *a bunch* of files will start to be installed into the current directory. It may seem very daunting and confusing at first, but we will go through the critical files that you *might* need to worry one by one. The rest are mostly irrelevant.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

`src/app/`

This is where you define what visitors see when they go to different parts of your website.
Think of each file here as a different “screen” on your site. Every time you want the user to see something, you will have a `src/app/page.tsx` in which you will write code and formatted HTML that will represent the home screen of the website.
If you, per say, wanted to create an "About Us" page, you'd have to create the file located as `src/app/aboutus/page.tsx` with more code that will once again display the data you want.

---

`public/` (Static Files)

Any file you put here will be available as-is on your site.
Example: Put logo.png in public/, and it will be viewable at http://localhost:3000/logo.png.
It is quite common to place images, downloadable files, or even favicons in here.

---

`package.json` and `package-lock.json` (the project’s mess)

This file lists everything your project depends on (packages and libraries), plus scripts to run and build the site.
You will only need to worry about `package.json` as `package-lock.json` is fully managed by Next.js. `package.json` manages what is the very fundamental system of your application while still being handled by Next.js. 
Think of a car's steering wheel. While you do manage the wheel itself and command the car to go to one direction or another, the components of the car manage the underlying system that make the car do what you want it to do. That's what `package.json` is for you.

Now notice the structure and the following comments:
```js
{
  "name": "my-next-app", // name of the application. Modify.
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev", // <-- Important
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  // Here-on-down you don't worry about (probably, hopefully)
  "dependencies": {
    "next": "latest",
    "react": "latest",
    "react-dom": "latest"
  },
  "devDependencies": {
    "eslint": "latest",
    "eslint-config-next": "latest"
  }
}
```

The sub-json under the scripts key is where the important commands come in. The way they are set up indicate how they should be ran to start a specific process.
If you wanted to start testing and looking at the progress of your application in real time, you would execute that "dev" key command by its value: next dev. You'd run:
```bash
npm run dev
```
That starts the local "development server" for testing. 
The other processes we will look at down the line.

---

`styles/` 

Contains global styles (globals.css) and other style files.
Since you’re using Tailwind CSS, you’ll be editing globals.css to include Tailwind’s base setup.
Fonts and other global css modifications can be added here as well.

---

`src/app/layout.tsx` — 
This is your site’s master template. 
Notice that this is actual TypeScript. This file wraps around every page in your app, like a frame around a picture. Perfect for adding headers, footers, navigation bars, or global styling so you don’t repeat code on every page.

For example something like:

```ts
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <header>My Navigation Bar</header>
        <main>{children}</main>
        <footer>© 2025 My Company</footer>
      </body>
    </html>
  );
}
```

That places an element onto every `page.tsx` that we have on our project.

---

Everything else is either fully managed or irrelevant to you at the moment.

We will be using these files and tools in detail once we start building on the next module.