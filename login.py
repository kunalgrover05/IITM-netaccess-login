from mechanize import Browser
import urllib2

# New browser object
br = Browser()

# Open Login page
print "Logging in"
page = br.open( 'https://netaccess.iitm.ac.in/account/login' )
br.select_form( nr = 0 )

# Fill in the fields
br.form[ "userLogin" ] = "me12b033"
br.form[ "userPassword" ] = "#J5+1qOn"

# Submit to login
br.submit()

print "Approving your IP"
# Directly go to the approve page. Cookies taken care of by Mechanize browser
resp = br.open( 'https://netaccess.iitm.ac.in/account/approve' )

# Hardcoded response due to bad HTML on site
hardcoded_resp = '''
<form class="form-horizontal" method="post" action="/account/approve">
<fieldset>
<!-- Form Name -->
<legend>Authorization</legend>
<!-- Multiple Radios -->
<div class="form-group">
  <label class="col-md-4 control-label" for="radios">Duration</label>
  <div class="col-md-4">
  <div class="radio">
    <label for="radios-0">
      <input type="radio" name="duration" id="radios-0" value="1" checked="checked">
      60 minutes (recommended for public machines)
    </label>
  </div>
  <div class="radio">
    <label for="radios-1">
      <input type="radio" name="duration" id="radios-1" value="2">
      1 day (hostel zone)
    </label>
  </div>
  </div>
</div>
<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="approveBtn"></label>
  <div class="col-md-4">
    <button id="approveBtn" name="approveBtn" class="btn btn-primary">Authorize</button>
  </div>
</div>
</fieldset>
</form> 
'''

# Setting response for Page as the hardcoded response.
resp.set_data( hardcoded_resp )
br.set_response( resp )
# Filling the form using the hardcoded response
br.select_form( nr = 0 )
br.form[ 'duration' ] = [ '2' ]
response = br.submit()
print "Logged in for one day"
