
Now that you know how to create a base component, export and import said component, we will learn the basics of styling HTML.

If you have ever worked on coding raw HTML & CSS for webpages, you'd know that most of the time you will require a separate CSS file to style the elements that you place in the HTML file by importing the whole sheet.

Instead, Tailwind CSS does it a lot easier by maintain everything short and functional.
Suppose that you want to make a component that draws a 300x300 pixel red squared box in the middle of the screen, has a 5 pixel green outline, and changes background color to blue every time the user hovers over it.
Then our component would be:
```ts
const Box = () => {
    return (
        <>
        <div className="flex justify-center pt-[30px]"> {/* The positioning of the box is this*/}
            <div className="w-[300px] h-[300px] border border-green-300 border-[5px] bg-red-500
            hover:bg-blue-400 transition-all duration-400 ease-in-out"> {/* The actual box is this*/}
            </div>
        </div>
        </>
    );
}
export default Box;
```

Most important of all, observe the `className` strings, which is where we set instructions for styling separated by spaces; otherwise known as an `attribute`.
Tailwind shortens the names of the `declarations` to modify, so in a way you have to learn them. However, it is always helpful to find out how to act on a declaration based on its shortened name and usage using the internet, should you happen to forget.

For example, say I forgot how to increase the font size of a paragraph.
Then I would just look up "tailwind increase font" on the browser and it should give you an example to know to do `<p className="text-sm"> Some Text </p>` or even better `<p className="text-[24px]"> Some Text </p>` (https://tailwindcss.com/docs/font-size)

But lets analyze the declarations of our Box step by step...

```css
flex justify-center pt-[30px]
```
Creates a flexbox (https://www.w3schools.com/css/css3_flexbox.asp) that allows us to move things around. In this case, we will move our item to be centered horizontally with `justify-center` and we will do a simple padding top of 30 pixels relative to the item(s) above.

```css
w-[300px] h-[300px] border border-green-300 border-[5px] bg-red-500 hover:bg-blue-400 transition-all duration-400 ease-in-out
```

We will set the width and height of our box to be 300px. We will declare that this `declaration box` will have a `border` and that the border will be green-300 (shades and colors: https://tailwindcss.com/docs/colors). We will say that the border will be 5 pixels thick, the background of the box will be red-500 but when cursor hovers over, then the background attribute will be overridden by blue-400. We will try to animate any CSS property that’s capable of being animated using `transition-all`, and make it so that said animation eases in or out with the new color over the span of 0.4 seconds.

---

If you wanted to have a navigation bar on your main page, you would start with something similar to a wide box, then add the buttons to them, then add specific behavior to the buttons. In practice it would look something like this:

src/app/components/navigation/HomeNavBar.tsx <- Preferred Path. Just keep as tidy as possible.
```ts
import Link from "next/link";

const NavBar = () => {
    return (
        <>
            <div className="w-full h-[100px] border border-black border-[1px] bg-gray-700">
                <ul className="flex items-center space-x-8 text-black">
                    {/* For the buttons, consider making them their own components too */}
                    <li> {/* Button One - Home Pagem*/}
                        <Link
                        href="/"
                        className="hover:text-white transition duration-300 lexend-text pl-[20px]"
                        >
                    </li>
                    <li> {/* Button Two - About Us Page*/}
                        <Link
                        href="/aboutus"
                        className="hover:text-white transition duration-300 lexend-text pl-[20px]"
                        >
                    </li>
                    ...
                </ul>
            </div>

        </>
    );
}
```

src/app/page.tsx
```ts
import { NavBar } from "./components/navigation/HomeNavBar.tsx"

const HomePage = () => {
    return (
        <NavBar/>
    );
}
```

Until this point, you are now capable of fully designing a static webpage from the ground up. The next big step to learn will be applying reactive behavior through functions, calling/fetching APIs, and applying logic.