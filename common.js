/*
 * common.js — injects the shared <head> (stylesheets, MathJax config, meta)
 * and the site header/footer into every page, using native fetch (no jQuery).
 *
 * If a fetch fails, the page still renders its own content; the error is
 * logged to the console instead of breaking the whole page.
 */
(function () {
    "use strict";

    // <script> elements created via innerHTML never execute, so rebuild them
    // as fresh nodes (inline content or external src) before inserting.
    function makeScript(oldScript) {
        var s = document.createElement("script");
        if (oldScript.src) {
            s.src = oldScript.src;
            s.async = false;
        } else {
            s.textContent = oldScript.textContent;
        }
        return s;
    }

    // Move every child of `container` into `target`, re-creating <script>
    // nodes on the way so that they actually run.
    function moveChildren(container, target) {
        var scripts = [];
        while (container.firstChild) {
            var node = container.firstChild;
            if (node.tagName === "SCRIPT") {
                scripts.push(node);
            } else {
                target.appendChild(node);
            }
        }
        for (var i = 0; i < scripts.length; i++) {
            target.appendChild(makeScript(scripts[i]));
        }
    }

    function injectHead(html) {
        var container = document.createElement("div");
        container.innerHTML = html;

        // The first <p> in head.html is the navigation bar -> site header.
        var nav = container.querySelector("p");
        if (nav && !document.getElementById("header")) {
            var header = document.createElement("header");
            header.id = "header";
            header.className = "site-header";
            header.appendChild(nav);
            document.body.insertBefore(header, document.body.firstChild);
        }

        moveChildren(container, document.head);

        // Re-typeset math that may have been added by this injection.
        if (window.MathJax && window.MathJax.typesetPromise) {
            window.MathJax.typesetPromise();
        }
    }

    function injectFooter(html) {
        var footer = document.getElementById("footer");
        if (!footer) {
            return;
        }
        var container = document.createElement("div");
        container.innerHTML = html;
        moveChildren(container, footer);
    }

    function load(url, onOk) {
        fetch(url)
            .then(function (response) {
                if (!response.ok) {
                    throw new Error(url + " -> HTTP " + response.status);
                }
                return response.text();
            })
            .then(onOk)
            .catch(function (error) {
                console.warn("[site] could not load " + url, error);
            });
    }

    document.addEventListener("DOMContentLoaded", function () {
        load("/node_modules/head.html", injectHead);
        load("/node_modules/foot.html", injectFooter);
    });
})();
