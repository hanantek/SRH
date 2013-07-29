'use strict';

var reports = angular.module('reports', []).
	config(function($interpolateProvider) {
		//allow django templates and singular to co-exist
  		$interpolateProvider.startSymbol('[[');
  		$interpolateProvider.endSymbol(']]');
	});

reports.run(function($rootScope, $http) {
	//$http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});

function ReportController($scope, $http) {
	
	$scope.searchQuery = function() {
		$scope.$apply(function() {
			console.log($scope.queryParams);
			$http({method: 'GET', url: '/api/v1.0/search/?'+$scope.queryParams}).
            success(function(data, status, headers, config) {
                $scope.results = data;                  //set view model
            }).
            error(function(data, status, headers, config) {
                $scope.results = data || "Busqueda Fallida";
                $scope.status = status;
            });
		});
	}
}
ReportController.$inject = ['$scope', '$http'];