'use strict';

function AppController($scope, $rootScope, $window, User) {

}

AppController.$inject = ['$scope', '$rootScope', '$window', 'User']

function HomeController($scope, $rootScope) {
	$rootScope.title = 'Sistema de recursos humanos';
	$rootScope.menusel = "home";
	console.log('home');
}

HomeController.$inject = ['$scope', '$rootScope'];

function LoginController($scope, $rootScope) {
	$rootScope.title = 'Login';
	$rootScope.menusel = ""; 
	console.log('login');
}

LoginController.$inject = ['$scope', '$rootScope'];

function RegisterController($filter, $scope, $rootScope, $location, Restangular, User, $window) {

	$rootScope.title = "Perfil";
	$rootScope.menusel = "profile";

	$scope.newInfo = false;
	Restangular.all('personalinfo').getList({user:User.id}).then(
		function(personal) {
			$scope.personal = personal[0];
			if(!$scope.personal) {
				$scope.newInfo = true;
				$scope.personal = {user:User.id,names:null,last_names:null,nationality:null,
						document_type:null, document_number:null,sex:null, civil_state:null,
						phone:null, mobile:null, birth:null, address:null, image:null};
			}
		},
		function(response) {
			console.log('Error with status code', response.status);
		});

	$scope.itemsNationalities = Restangular.all('nationality').getList();
	$scope.itemsDocumenType = Restangular.all('document').getList();
	$scope.itemsGender = Restangular.all('gender').getList();
	$scope.itemsCivilState = Restangular.all('civilstate').getList();

	$scope.steps = ['Uno', 'Dos'];
	$scope.step = 0;

	$scope.isFirstStep = function() {
		return $scope.step === 0;
	}

	$scope.isLastStep = function() {
		return $scope.step === ($scope.steps.length - 1)
	}

	$scope.isCurrentStep = function(step) {
		return $scope.step === step
	}

	$scope.setCurrentStep = function (step) {
		$scope.step = step;
	}

	$scope.getCurrentStep = function() {
		return $scope.steps[$scope.step];
	}

	$scope.getNextLabel = function() {
		return ($scope.isLastStep()) ? 'Enviar' : 'Siguiente';
	};

	$scope.handlePrevious = function() {
		$scope.step -= ($scope.isFirstStep()) ? 0 : 1;
	}
	
	$scope.handleNext = function(dismiss) {
		if($scope.isLastStep()) {
			console.log("Antes de guardar");
			if ($scope.newInfo) {
				$scope.personal.birth = $filter('date')($scope.personal.birth, 'yyyy-MM-dd');
				Restangular.all('personalinfo').post($scope.personal);
			} else {
				$scope.personal.put();
			}

			dismiss();
		} else {
			$scope.step += 1;
		}
	}
}

RegisterController.$inject = ['$filter', '$scope', '$rootScope', '$location', 'Restangular', 'User'];

