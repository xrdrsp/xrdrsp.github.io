document.write('<script src="/node_modules/jquery.js"></script>');

document.addEventListener("DOMContentLoaded", function() {
    $.get("/head.html", function(htmlData) {
        var $temp = $("<div>").html(htmlData);

        var $nav = $temp.find("p").first(); 
        if ($nav.length > 0) {
            var $header = $('<header id="header" class="site-header"></header>').append($nav);
            $("body").prepend($header);
        }

        $temp.find("p").first().remove(); 

        $("head").append($temp.html());

        if (window.MathJax && window.MathJax.typesetPromise) {
            MathJax.typesetPromise();
        }
    });

    var $footerContainer = $("#footer");
    if ($footerContainer.length > 0) {
        $footerContainer.load("/foot.html");
    }
});