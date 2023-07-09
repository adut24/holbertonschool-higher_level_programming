$(document).ready(() => {
  const fetchTranslation = () => {
    const lang = $('#language_code').val();
    $.get(`https://stefanbohacek.com/hellosalut/?lang=${lang}`, data => {
      $('#hello').html(data.hello);
    });
  };

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(event => {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
