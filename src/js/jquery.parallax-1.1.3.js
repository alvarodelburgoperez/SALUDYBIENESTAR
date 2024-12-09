/*
 Plugin: jQuery Parallax
 Version 1.1.3
 Author: Ian Lunn
 Twitter: @IanLunn
 Author URL: http://www.ianlunn.co.uk/
 Plugin URL: http://www.ianlunn.co.uk/plugins/jquery-parallax/

 Dual licensed under the MIT and GPL licenses:
 http://www.opensource.org/licenses/mit-license.php
 http://www.gnu.org/licenses/gpl.html
 */

(function ($) {
    var $window = $(window);
    var windowHeight = $window.height();

    $window.resize(function () {
        windowHeight = $window.height();
    });

    $.fn.parallax = function (xpos, speed, offset, outerHeight) {
        var $this = $(this);
        var getHeight;
        var paddingTop = 0;
        var speedFactor = speed;
        var offset = offset ? parseInt(offset) : null;


        if (outerHeight) {
            getHeight = function (jqo) {
                return jqo.outerHeight(true);
            };
        } else {
            getHeight = function (jqo) {
                return jqo.height();
            };
        }


        // setup defaults if arguments aren't specified
        if (arguments.length < 1 || xpos === null) xpos = "50%";
        if (arguments.length < 2 || speedFactor === null) speedFactor = -0.2;
        if (arguments.length < 3 || offset === null) offset = 0;
        if (arguments.length < 4 || outerHeight === null) outerHeight = true;

        // function to be called whenever the window is scrolled or resized
        function update() {

            var pos = $window.scrollTop();
            $this.each(function () {
                var $element = $(this);
                var top = $element.offset().top;
                var height = getHeight($element);
                // Check if totally above or totally below viewport
                if (top + height < pos || top > pos + windowHeight) {
                    return;
                }

                $this.css('backgroundPosition', xpos + " " + (Math.round((top - pos) * speedFactor) + offset) + "px");
            });
        }

        $window.bind('scroll', update).resize(update);
        update();
    };
})(jQuery);

$(document).ready(function () {
    var obj;
    if ((obj = $('.parallax')).length > 0 && $('html').hasClass('desktop')) {
        for (var i = 0; i < obj.length; i++) {

            $(obj[i]).parallax("50%", obj[i].getAttribute('data-parallax-speed'), obj[i].getAttribute('data-parallax-offset'));
        }
    }
});
