angular.module('srh.routes', []).config(['$routeProvider', function($routeProvider) {
		$routeProvider.when('/login', {templateUrl: '/static/partials/login.html', controller: 'LoginController'});
		$routeProvider.when('/', {templateUrl: '/static/partials/index.html', controller: 'HomeController'});
		$routeProvider.otherwise({redirectTo: '/'});
	}]);