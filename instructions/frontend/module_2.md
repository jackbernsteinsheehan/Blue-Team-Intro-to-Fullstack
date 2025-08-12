
You will be solely working under the `src/app/` directory, but as a reminder, ensure to work under the `frontend/` directory for everything to function perfectly. To ensure that you are in the correct place, type the `pwd` command on the terminal. You should see something like:
```
/Users/.../Intro-to-Fullstack/frontend
```
or if you see that you are at the root of the project, go ahead and simply do `cd frontend` that will take you to the working directory where Next.js will be installed.

Now run `npm run dev` on the terminal. You should see something like:

```bash
> project_name@0.1.0 dev
> next dev --turbopack

   ▲ Next.js 15.3.2 (Turbopack)
   - Local:        http://localhost:3000
   - Network:      http://172.20.10.10:3000
   - Environments: .env.local

 ✓ Starting...
 ✓ Ready in 1526ms
```
Which indicates that your project is running the development server locally on port 3000.
Open the specified URL: `http://localhost:3000` in the browser. Here you will see the templated main home page that Next.js has created for you (src/app/page.tsx is where everything is located code-wise).

Now that your terminal is in the correct place and you are working under `src/app/`, create a directory and call it `components` (src/app/components).

A react component can be thought of as a class with its respective attributes in the form of variables, methods in the form of internal functions, and a final return value in the form of formatted, event-driven HTML consolidating everything together.
Components consolidate this "reactive" HTML to be used over and over again in the main display `page.tsx` screens. It's a great way to maintain clean and readable code.

Enough talk...

Begin by imagining what you want your home page to look like .
Got it?
Now start from top-down and think of every element you want home page to have.

For example, a navigation bar is quite common.
Lets start with that.
psd. Keep the dev server running, no problem.

Under your components directory create the `NavBar.tsx` file. *You are allowed to name your component files anything you'd like. But remember that actual pages to be seen by the users **must be called page.tsx strictly***

Initialize this component the same way you would create a JavaScript function:

```ts
const NavBar = () => { // preferred
}
or
function NavBar() {
}
```
and the function should always return HTML like:
```ts
const NavBar = () => {
    return (
        <> {/* <-- Important */}
        <div>
            <button>
            ...
            </button>
        </div>
        <div>
        ...
        </div>
        </> {/* <-- Important */}
    );
}
```

Suppose you wanted to pass a parameter that will dynamically change the color and add some text of some value inside of our component. Then...

```ts
const SomeSquare = ({color, text} : {color:string; text:string}) => {
    return (
        <>
        <div style={{ backgroundColor: color, width: 500px, height: 500px}}>
            <h1>{text}</h1>
        </div>
        </>
    )
}

export default SomeSquare; // ESSENTIAL!!! Otherwise it won't work!! Exporting our main component.
```
And to actually display this component for the user to see in some `page.tsx`, then you would do:
```ts
import { SomeSquare } from "./components/ComponentFileName.tsx"; 

const AboutUsPageSample = () => {
    return (
    <SomeSquare/> // without parameters passed (not valid in our case)
    <SomeSquare color="red" text="Some nice text here"/> // with parameters
    );
}
```

On the next module, we will help you get started on Tailwind CSS styling, package installation, and font installation.