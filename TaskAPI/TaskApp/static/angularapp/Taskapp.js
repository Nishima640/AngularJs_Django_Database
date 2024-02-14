var Taskapp = angular.module('Taskapp',[]);

app.controller('TaskappController',['$scope', '$http',function($scope,$http){


    $scope.Add = function() {
        
        var data={
            'SubjectA' : $scope.SubjectA,
            'SubjectB' : $scope.SubjectB
        };

        
        $http.post('http://127.0.0.1:8000/tables/'+ data.SubjectA + '/' + data.SubjectB+'/' ,data,{
        // $http({
        //     method : "POST",
        //     url : "http://127.0.0.1:8000/tables/"
        //     params: {SubjectA:data.SubjectA}

            

        }).then(function(response){
            $scope.Total = response.data.Total;
            $scope.Average = response.data.Average;
        })

        
    } 
}])