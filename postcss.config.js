const tailwindcss = require("tailwindcss");

const isProduction = process.env.NODE_ENV === "development";
const plugins = [tailwindcss];

// TODO: add purgecss
// The purgecss rules are from this blog post:
// https://medium.com/@adisk/how-to-setup-tailwind-css-with-parcel-bundler-f76e4aac5f16
// It doesn't look like it will work with Django without modifiction, so it
// would need to be edited.
// if (isProduction) {
//     const purgecss = require("@fullhuman/postcss-purgecss-purgecss");
//     class TailwindExtractor {
//         static extract(content) {
//             return content.match(/[A-z0-9-:\/]+/g) || [];
//         }
//     }

//     plugins.push(
//         purgecss({
//             content: ["src/*.html"],
//             extractors: [
//                 {
//                     extractor: TailwindExtractor,
//                     extensions: ["html"],
//                 },
//             ],
//         })
//     );
// }

module.exports = {
    plugins,
};