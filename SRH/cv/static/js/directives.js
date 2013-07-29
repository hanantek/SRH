/*app.directive('timeAgo', function($timeout) {
	return {
		restrict: 'A',
		scope: {
			title: '@'
		},
		link: function(scope, elem, attrs) {
			var updateTime = function() {
				if(attrs.title) {
					elem.text(moment(attrs.title).fromNow());
					$timeout(updateTime, 15000);
				}
			};
			scope.$watch(attrs.title, updateTime);
		}
	};
});*/

app.directive('pendingbar', function($rootScope) {
	return {
		link: function(scope, element, attrs) {
			element.addClass('hide');
			$rootScope.$on('$routeChangeStart', function() {
				element.removeClass('hide');
			});
			$rootScope.$on('$routeChangeSuccess', function() {
				element.addClass('hide');
			});
			$rootScope.$on('$routeChangeError', function() {
				element.removeClass('hide');
			});
		}
	};
});

app.directive('viewstate', function($rootScope) {
	return {
		link: function(scope, element, attrs) {
			element.addClass('hide');
			$rootScope.$on('$routeChangeStart', function() {
				element.addClass('hide');
			});
			$rootScope.$on('$routeChangeSuccess', function() {
				element.removeClass('hide');
			});
			$rootScope.$on('$routeChangeError', function() {
				element.addClass('hide');
			});
		}
	};
});

app.directive('viewstate', function($rootScope, $location, User, $window) {
	return {
		link: function(scope, elem, attrs, ctrl) {
			$rootScope.$on('$routeChangeStart', function(event, current, next){
				console.log('User: '+User.username+'/'+User.id);
				if (!User.isAuthenticated) {
					$window.location.href = "/home/";
				}
				
			});
		}
	}
});