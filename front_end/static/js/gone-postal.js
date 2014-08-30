(function(){
    var app = angular.module('postal', []);
    
    app.controller('ResultsController',function(){
        this.items = saves;
        console.log(this)
    });
    
//I think this is the code needed to read in data from a JSON file, it doesn't work locally because of browser security. ReQuires a small change to the html     
    app.controller('findResults', function($scope,$http){
        result = this
        dummy = {
                  "savings_targets": [{"name": "NY trip","amount": 120.00,"date": "2014-09-12"},
                                      {"name": "New shoes","amount": 1300.00,"date": "2014-11-03"}
                                     ],
                  "existing_savings": 134.26,
                  "session_id": "ae98-08c2-bd39-a167"
                }
                   $http.post('monthly_sample.json', dummy)
                        .then(function(res){
                            result.items = res.data.result_data
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
    