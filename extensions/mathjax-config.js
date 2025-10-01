// Archive only

window.MathJax = {
    tex: {
        inlineMath: {'[+]': [['$', '$']]}
    },
    loader: {load: ["input/tex", "output/chtml"]},
    output: {
        displayOverflow: 'linebreak',  // break long lines
        linebreaks: {                  // options for when overflow is linebreak
            inline: true,                   // true for browser-based breaking of in-line equations
            width: '100%',                  // a fixed size or a percentage of the container width
            lineleading: .2,                // the default lineleading in em units
            LinebreakVisitor: null,         // The LinebreakVisitor to use
        },
        font: 'mathjax-modern'
    },
    options: {
        enableExplorer: false,
        enableMenu: true,
        menuOptions: {
            settings: {
                showSRE: false,        // true to include semantic attributes in MathML output
                showTex: false,        // true to include original LaTeX commands in MathML output
                texHints: true,        // put TeX-related attributes on MathML
                semantics: false,      // put original format in <semantic> tag in MathML
                zoom: 'DoubleClick',        // or 'Click' or 'DoubleClick' as zoom trigger
                zscale: '200%',        // zoom scaling factor
                renderer: 'CHTML',     // or 'SVG'
                alt: false,            // true if ALT required for zooming
                cmd: false,            // true if CMD required for zooming
                ctrl: false,           // true if CTRL required for zooming
                shift: false,          // true if SHIFT required for zooming
                scale: 1,              // scaling factor for all math
                overflow: 'Scroll',    // how to handle math that is wider than its container
                breakInline: true,     // true to allow automatic line breaks with in-line math
                inTabOrder: true,      // true if tabbing includes math

                enrich: true,          // true if semantic-enrichment should be performed
                collapsible: false,     // true if complex math should be collapsible
                assistiveMml: false,    // true if hidden assistive MathML should be generated for screen readers

                // also these a11y options from the explorer extension

                a11y: {
                    speech: true,               // switch on speech output
                    braille: true,              // switch on Braille output
                    subtitles: true,            // show speech as a subtitle
                    viewBraille: true,         // display Braille output as subtitles
                    help: true,                 // include "press h for help" messages on focus
                    roleDescription: 'math',    // the role description to use for math expressions
                    voicing: false,             // switch on speech output

                    backgroundColor: 'Blue',    // color for background of selected sub-expression
                    backgroundOpacity: .2,      // opacity for background of selected sub-expression
                    foregroundColor: 'Black',   // color to use for text of selected sub-expression
                    foregroundOpacity: 1,       // opacity for text of selected sub-expression

                    highlight: 'Hover',          // type of highlighting for collapsible sub-expressions
                    treeColoring: false,        // tree color expression

                    magnification: 'None',      // type of magnification
                    magnify: '400%',            // percentage of magnification of zoomed expressions

                    infoType: false,            // show semantic type on mouse hovering
                    infoRole: false,            // show semantic role on mouse hovering
                    infoPrefix: false          // show speech prefixes on mouse hovering
                }
            },
            annotationTypes: {
                TeX: ['TeX', 'LaTeX', 'application/x-tex'],
                StarMath: ['StarMath 5.0'],
                Maple: ['Maple'],
                ContentMathML: ['MathML-Content', 'application/mathml-content+xml'],
                OpenMath: ['OpenMath']
            }
        }
    }
};