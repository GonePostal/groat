(function(){
    var app = angular.module('postal', []);
    
    app.controller('ResultsController',function(){
        this.items = saves;
        console.log(this)
    });
       
    app.controller('findResults', function($scope,$http){
        result = this
        dummy = {
                  "savings_targets": [{"name": "NY trip","amount": 120.00,"date": "2014-09-12"},
                                      {"name": "New shoes","amount": 1300.00,"date": "2014-11-03"}
                                     ],
                  "existing_savings": 134.26,
                  "session_id": "ae98-08c2-bd39-a167"
                }
        
        ///test = makejson()
        
                   $http.post('monthly_sample.json', dummy)
                        .then(function(res){
                            result.items = res.data.result_data
                    });
    });        
})();


$.fn.serializeGroups=function(){
    var results=[];
    $(this).find('.form-group-1').each(function(){
        var o={};
        $(this).find('input').each(function(){
            o[this.name]=this.value;
        });
        results.push(o);        
    });
    $(this).find('.form-group-2').each(function(){
        var o={};
        $(this).find('input').each(function(){
            o[this.name]=this.value;
        });
        results.push(o);        
    });   
    return results;
}


$(function makejson() {
    $('#form_saving_for').submit(function() {
        var groups = $('#form_saving_for').serializeGroups();
        var data = {};
        data["savings_targets"]=[data["savings_targets"]];
        data.savings_targets=groups;
        data["existing_savings"]=[data["existing_savings"]];
        data.existing_savings= $('#existing_savings').prop('value')
        data["session_id"]=[data["session_id"]];
        data.session_id = "ae98-08c2-bd39-a167";        
        $('#result_2').html(JSON.stringify(data));
        return data;
    });
});


        
    