(function($) {
    $(function() {
        /**
         * Menu actions
         */
        $menu = $(".menu");
        $content = $(".content");

        $menu.find(".navbar a").on("click", function() {
            if ($menu.hasClass("menu-extended")) {
                $menu.find(".app-name, .app-arrow").hide();
                $menu.find(".app-model").removeClass("show");
                
                $menu.animate({width: '3.1rem'}, function() {
                    $menu.removeClass("menu-extended");
                    $menu.addClass("menu-collapsed");
                });
                $content.animate({"margin-left": '3.1rem'});
            
            } else {
                $menu.animate({width: '15rem'}, function() {
                    $menu.find(".app-name, .app-arrow").show();
                    $menu.addClass("menu-extended");
                    $menu.removeClass("menu-collapsed");
                });
                $content.animate({"margin-left": '15rem'});
            }
        });

        $menu.find(".app-model").on("show.bs.collapse", function() {
            if (!$menu.hasClass("menu-extended")) {
                $menu.find(".navbar a").click();
            }
        })
    })
})(jQuery)