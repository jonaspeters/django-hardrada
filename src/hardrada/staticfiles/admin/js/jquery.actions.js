(function($) {
    $(function() {
        /**
         * Menu actions
         */
        $menu = $(".menu");
        $header = $(".header");
        $content = $(".content");

        /**
         * Toogle menu
         */
        var toogleMenu = function() {
            var isExtended = $menu.hasClass("menu-extended");

            if (isExtended) {
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
        }

        /**
         * Save menu preference and toogle menu
         */
        $menu.find(".navbar a").on("click", function() {
            var isExtended = $menu.hasClass("menu-extended");
            
            // send post for set menu preference in session
            $.post(window.__hardrada_menu__, {extended: !isExtended}, function(data) {
                toogleMenu();
            });
        });

        /**
         * Open app menu em toogle menu
         */
        $menu.find(".app-model").on("show.bs.collapse", function() {
            if (!$menu.hasClass("menu-extended")) {
                toogleMenu();
            }
        })

        /**
         * Change theme
         */
        $header.find("#change-theme").on("click", function() {
            var theme = $("html").attr("data-bs-theme");
            $.post(window.__hardrada_theme__, {theme: theme}, function() {
                location.reload();
            })
        })

        /**
         * Document events
         */
        $( document ).on( "click", function( event ) {
            if ($(event.target).closest("#profile-tools").length === 0) $("#profile-tools").collapse("hide");
          });
    })
})(jQuery)