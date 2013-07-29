'use strict';

// Declare app level module which depends on filters, and services

var app = angular.module('srh', ['ngCookies', 'ngResource','$strap.directives', 'restangular']).
	config(function($interpolateProvider, $routeProvider, RestangularProvider) {
		//allow django templates and singular to co-exist
  		$interpolateProvider.startSymbol('[[');
  		$interpolateProvider.endSymbol(']]');

  		RestangularProvider.setBaseUrl("/api/v1.0");
		RestangularProvider.setRequestSuffix('/');

  		$routeProvider.when('/cv', {templateUrl: 'static/partials/profile.html', controller: 'RegisterController'});
  		$routeProvider.when('/login', {templateUrl: 'static/partials/login.html', controller: 'LoginController'});
		$routeProvider.when('/', {templateUrl: 'static/partials/index.html', controller: 'HomeController'});
		$routeProvider.otherwise({redirectTo: '/'});
	});

app.run(['$rootScope', '$http', '$cookies',function($rootScope, $http, $cookies) {
	$http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
	console.log($http.defaults.headers.common['X-CSRFToken']);
}]);

app.value('$strapConfig', {
	datepicker: {
		language: 'en',
		format: 'yyyy M d'
	}
});