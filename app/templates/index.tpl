%rebase('templates/layout.tpl', title='Home')
        <div class="page-header">
            <h1>Page Header</h1>
        </div>
         <div class="row">
            <div class="col-md-12" style="text-align: center;">
                <p>Body</p>
                <p>{{test_message}}</p>
                <p>
                    Your location: Lon: {{location[0]}}, Lat: {{location[1]}}
                </p>
            </div>
        </div>
