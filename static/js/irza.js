$(document).ready(function()
{
  $("div.flash").delay(5000).fadeOut();
  $("table#table-custom-2 tbody tr:even").css("background-color", "#C2F4F8");
  $("table#table-custom-2 tbody tr:odd").css("background-color", "#EFB1F1");
  $("table#table-custom-1 tbody tr:even").css("background-color", "#C2F4F8");
  $("table#table-custom-1 tbody tr:odd").css("background-color", "#EFB1F1");
});
