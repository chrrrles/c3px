# Copyright (c) 2013 - The C3PX authors.
#
# This file is part of C3PX.
#
# C3PX is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as 
# published by the Free Software Foundation, either version 3 of 
# the License, or (at your option) any later version.
#
# C3PX is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public 
# License along with C3PX.  If not, see <http://www.gnu.org/licenses/>.

firstnames = [
  'Robert', 'Michael', 'Kelly', 'Anna', 'Jeffrey', 'Mitchell', 'Charles', 'Thomas', 'John', 'Fred', 'Samson', 'Linda', 'Julie', 'Margaret', 'Noel', 'Timothy', 'Jennifer', 'Christopher', 'Chris']

lastnames = [
  'Thompson', 'Paul', 'Stevenson', 'Dahl', 'Lennon', 'Cook', 'Adams', 'Finch', 'Lubbock', 'Danielson', 'Richardson', 'Davids', 'Stone', 'Carter', 'Deeds', 'Raymond', 'Cohen', 'Washington', 'Chung']

email_hosts = [
  'gmail.com', 'hotmail.com', 'ghana.com', 'qq.com', 'yahoo.com', 'riseup.net', 'bbchat.com']

street_names = [ 
  "Ice-cream", "Insect", "Jetfighter", "Junk", "Kaleidoscope", "Kitchen", "Knife", "Leatherjacket", "Leg", "Library", "Liquid", "Magnet", "Man", "Map", "Maze", "Meat", "Meteor", "Microscope", "Milk", "Milkshake", "Mist", "Software", "Solid", "Space Shuttle", "Spectrum", "Sphere", "Spice", "Spiral", "Spoon", "Sports-car", "Spot Light", "Square", "Staircase", "Star", "Stomach", "Sun", "Sunglasses"]

road_types = [ 'Lane', 'Street', 'Avenue', 'Blvd.', 'Way']

cities = [
  "Indianapolis  ", "Iowa City ", "Jacksonville  ", "Jamestown ", "Jersey City", "Johnson City  ", "Junction  ", "Kennewick ", "Kenosha ", "Key West", "Kissimmee ", "Knoxville ", "Kodiak  ", "Laconia ", "Lafayette", "Lakewood  ", "Lancaster ", "Lansing ", "Las Vegas ", "Laughlin", "Lawrence  ", "Lincoln ", "Littleton ", "Lompoc  ", "Long Beach", "Long Branch ", "Los Angeles ", "Lubbock ", "Valdosta  ", "Vicksburg ", "Villas  ", "Vineland  ", "Walla Walla", "Washington  ", "Waterloo  ", "Weatherford ", "Wenatchee ", "Windsor", "Woonsocket  ", "Worthington ", "Yakima  ", "Yankton ", "Youngstown", "Yuma         ", "Abbeville ", "Aaberdeen ", "Abilene ", "Akron ", "Albany", "Alexandria  ", "Allentown ", "Amarillo  ", "Anaheim ", "Anchorage", "Anderson  ", "Ann Arbor ",
  "Annapolis ", "Anniston  ", "Arlington", "Asheville ", "Ashland ", "Astoria ", "Athens  ", "Atlanta", "Atlantic  ", "Augusta ", "Austin  ", "Bakersfield ", "Baltimore"]

states = {  # we use valid zip codes for geolocation
  'AK' : [
    "99501", "99502", "99503", "99504", "99505", "99506", "99507", "99508", "99509", "99510", "99511", "99512", "99513", "99514", "99515", "99516", "99517", "99518", "99519", "99520", "99521", "99522", "99523", "99524", "99540", "99546", "99547", "99548", "99549", "99550", "99551", "99552", "99553", "99554", "99555", "99556", "99557", "99558", "99559", "99561", "99563", "99564", "99565", "99566", "99567"], 
  'CA' : [
    "90003", "90004", "90005", "90006", "90007", "90008", "90009", "90010", "90011", "90012", "90013", "90014", "90015", "90016", "90017", "90018", "90019", "90020", "90021", "90022", "90023", "90024", "90025", "90026", "90027", "90028", "90029", "92021", "92022", "92023", "92024", "92025", "92026", "92027", "92028", "92029", "92030", "92033", "92036", "92037", "92038", "92039", "92040", "92046", "92049", "92051", "92052", "92054", "92055", "92056", "92057", "92058", "92059", "92060", "92061", "92064", "92065", "92066", "92067", "92068", "92069", "92070", "92071", "92072", "92074", "92075", "92078", "92079", "92082", "92083", "92084", "92085", "92086", "92088", "92090", "92091"],
  'NY' : [
    "10001", "10002", "10003", "10004", "10005", "10006", "10007", "10008", "10009", "10010", "10011", "10012", "10013", "10014", "10015", "10016", "10017", "10018", "10019", "10020", "10021", "10022", "10023", "10024", "10025", "10026", "10027", "10028", "10588", "10589", "10590", "10591", "10592", "10594", "10595", "10596", "10597", "10598", "10601", "10602", "10603", "10604", "10605", "10606", "10607", "10610", "10625", "10629", "10633", "10650", "10701", "10702", "10703", "10704", "10705", "10706", "10707", "10708", "10709", "10710", "10801", "10802", "10803", "10804", "10805", "10901", "10910", "10911", "10912", "10913", "10914", "10915", "10916", "10917", "10918", "10919", "10920", "10921", "10922", "10923", "10924", "10925", "10926", "10927", "10928", "10930", "10931", "10932", "10933", "10940"] }
