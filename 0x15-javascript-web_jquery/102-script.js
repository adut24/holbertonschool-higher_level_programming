document.addEventListener('DOMContentLoaded', () => {
  $('#btn_translate').click(() => {
    const lang = $('#language_code').val();
    $.get('https://stefanbohacek.com/hellosalut/?lang=' + lang, data => {
      $('#hello').html(data.hello);
    });
  });
});
