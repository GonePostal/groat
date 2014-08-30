(function(){
    var app = angular.module('postal', []);
    
    app.controller('ResultsController',function(){
        this.items = saves;
    });
    
//I think this is the code needed to read in data from a JSON file, it doesn't work locally because of browser security. ReQuires a small change to the html     
    app.controller('findResults',function($scope,$http){
                   $http.get('monthly_sample.json')
                        .then(function(res){
                            $scope.monthly_sample = res.data
                    });
    });
        
    var saves = [  
      {
        month: "1st September 2014",
        amount: 280, 
      },    
      {
          month:"1st October 2014",
          amount: 210, 
      }, 
      
      {
          month:"1st November 2014",
          amount:210,
      },
        
      {
          month:"1st December 2014",
          amount:140,
      },        
        
      {
          month:"1st January 2015",
          amount:80,
      },        
        
    ]; 
        
})();    
    