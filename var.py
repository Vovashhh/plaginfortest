# Стоит ли переделывать переменные под словарь ...

#pathToPlagin = "C:/Users/crm.28540/Desktop/USP_Plugin" #"/Users/max/Downloads/USP_Plugin"
pathToPlagin = "C:/Users/crm.28540/Documents/plugin"

i = 2

urlHabr = "https://freelance.habr.com"
urlHabrNew = 'https://freelance.habr.com/tasks/584412'
nameUrlHabr = 'Небольшая задача по написанию команды ADB на Kotlin для Android'

urlHabrRegMe = "https://freelance.habr.com/tasks/580546"  # зарегестрированна за мной
urlHabrRegNotMe = "https://freelance.habr.com/tasks/578786"  # зарегана не мной
urlHabrRegMeSendUSP = "https://freelance.habr.com/tasks/577246"  # Отправил УТП я
urlHabrRegNotMeSendUSP = "https://freelance.habr.com/tasks/578566"  # Отправил УТП не я
#--------

urlKwork = "https://kwork.ru/"
urlKworkNew = 'https://kwork.ru/projects/2501519'
nameUrlKwork = 'Трафик на сайт'

urlKworkRegMe = "https://kwork.ru/projects/2480675/view"  # зарегестрированна за мной
urlKworkRegNotMe = "https://kwork.ru/projects/2460455/view"  # зарегана не мной
urlKworkRegMeSendUSP = "https://kwork.ru/projects/2445384/view"  # Отправил УТП я
urlKworkRegNotMeSendUSP = "https://kwork.ru/projects/2469228/view"  # Отправил УТП не я
#--------

urlFreelance = "https://freelance.ru/"
urlFreelanceNew = 'https://freelance.ru/projects/planirovki-domov-gotovim-renderam-starim-planirovkam-edinom-stile-1563261.html'
nameUrlFreelance = 'Планировки домов по готовым рендерам и старым планировкам в едином стиле для каталога'

urlFreelanceRegMe = "https://freelance.ru/projects/sozdanie-sajta-skupka-problemnih-avto-na-tilde-1576785.html"  # зарегестрированна за мной
urlFreelanceRegNotMe = ""  # зарегана не мной
urlFreelanceRegMeSendUSP = "https://freelance.ru/projects/sdelat-portfolio-dlya-nok-norpriz-1578473.html"  # Отправил УТП я
urlFreelanceRegNotMeSendUSP = "https://freelance.ru/projects/razrabotat-dizajn-dlya-platformi-dlya-prodazhi-odezhdi-1564116.html"  # Отправил УТП не я
#--------

urlFreelancer = 'https://www.freelancer.com/'
urlFreelancerNew = 'https://www.freelancer.com/projects/shopify-site/woocommerce-shopify-migration-with-new'
textFreelancer = 'Woocommerce to Shopify Migration with New Design'

urlFreelancerRegMe = "https://www.freelancer.com/projects/python/TradeTron-custom-strategy-builder-for-37642435/details"  # зарегестрированна за мной
urlFreelancerRegNotMe = ""  # зарегана не мной
urlFreelancerRegMeSendUSP = "https://www.freelancer.com/projects/website-design/Custom-Landing-Page-Design/details"  # Отправил УТП я
urlFreelancerRegNotMeSendUSP = "https://www.freelancer.com/projects/c-sharp-programming/Test-project-for/details"  # Отправил УТП не я

# Переменные селекторов

btnCompany = "//select/option[2]"

# Спарсить все сообщения (HABR) - ID
msgParsingBtn = "btn-message-parse"
# "Парсинг сообщений завершен" в модальном окне парсинга (HABR) XPATH
parsingEnd = "//div[contains(text(), 'Парсинг завершен')]"
# Закрыть модальное окно парсинга сообщений (HABR) CLASS_NAME
parsModalClose = "plugin-modal-close"
# Автовход XPATH
autoLogin = "//button[contains(text(), 'Автовход') and not(contains(text(), 'по сессии'))]"
# Автовход по сессии XPATH
sessionLogin = "//button[contains(text(), 'Автовход по сессии')]"
# Колоколчик CSS_SELECTOR
alertBellBut = "div.plugin-notification-button"
# Форма колокольчика CLASS_NAME
bellForm = "plugin-notification-popup-container"
# Пользователи ID
bellUser = "user-block-container"
# Пользователь зарегистрировал проект XPATH
userRegProj = "//div[contains(., 'Пользователь')][contains(., 'зарегистрировал проект')]"
# Вы зарегистрировали проект XPATH
regProjByMe = "//div[contains(text(), 'зарегистрировали проект')]"
# Вы отправили УТП XPATH
sentUTP = "//div[contains(text(), 'отправили УТП')]"
# Пользователь &&& отправил УТП XPATH
otherUserSentUSP = "//div[contains(., 'Пользователь')][contains(., 'отправил УТП')]"
# Форма когда несколько пользователей на одной заявке XPATH
multiUserForm = "//div[contains(., 'Пользователь')][contains(., 'сейчас на этой странице проекта')]"
# Кружок DzenCode (на зарег заявке) ID
dzenCirle = "btn-plugin"
# Вкладка история CLASS_NAME
dzenHistoryTab = "plugin-info-button-tab.active"
# Фото CLASS_NAME
dzenPhotoStory = "plugin-info-icon-block"
# ФИО CLASS_NAME
dzenHistoryFullName = "plugin-info-name"
# ID CLASS_NAME
dzenHistoryID = "plugin-info-description"
# Название действия CLASS_NAME
dzenAction = "plugin-info-info-block-name"
# Дата CLASS_NAME
dzenDate = "plugin-info-info-block-date"
# Иконка действия CLASS_NAME
dzenIconAct = "plugin-info-state-block"
# Подробнее CLASS_NAME
dzenHistMore = "plugin-info-bottom-btn"
# Вкладка GPT CSS_SELECTOR
mainGPT = "div.plugin-info-button-tab.gpt"
# Форма формирования CLASS_NAME
formGPT = "plugin-message-gpt-answer"
# Выпадающий список ID ID
listGPT = "select-role"
# Копировать CLASS_NAME
copyGPT = "copy-icon"
# Кнопка получить CLASS_NAME
getGPT = "plugin-gpt-bottom-btn"
# Вкладка Информация XPATH
dzenInfo = "//div[contains(@class, 'plugin-info-button-tab') and text()='Информация']"
# форма информации о статусе заявки
dzenInfoFormHarb = "/html/body/div[7]/div[2]/div[1]/div"
# CLASS_NAME
dzenInfoKwork = "plugin-project-content-modal-body"
# Информация о клиенте ID
clientInfoBtn = "plugin-client-info"
# Клиент CLASS_NAME
clientIcon = "plugin-client-popup-title"
# Статистика заявок CLASS_NAME
reqStats = "plugin-client-popup-statistic-title"
# В процессе XPATH
reqStestProgress = "//div[@class='plugin-client-stats-name'][contains(., 'В процессе:')]"
# Завершены по причине: XPATH
closedReason = "//div[contains(@class, 'plugin-client-stats-name')][contains(text()," " 'Завершены по причине:')]"
# Завершены сделкой XPATH
compByDeal = "//div[contains(@class, 'plugin-client-stats-name')][contains(text(), 'Завершены сделкой:')]"
# Кнопка ввода комментария CLASS_NAME
commentBtn = "clent-info-icon"
# Форма ввода комментария ID
commentForm = "plugin-comment-textarea"
# Отмена CLASS_NAME
cancelClient = "btn-moderation-client-close"
# Сохранить CLASS_NAME
saveClient = "btn-moderation-client-send"
# Закрытие формы CLASS_NAME
closeClient = "close-message-client"
# Кнопка сообщения ID
messegeBtn = "btn-chat-url"
# Отправка УТП на модерацию ID
uspModeration = "btn-moderation-plugin"
# Кнопка отправить CLASS_NAME
uspSend = "btn-moderation-primary-send"
# Кнопка отмена CLASS_NAME
uspCancel = "btn-moderation-primary-close"
# Форма УТП ID
uspForm = "plugin-message-textarea"
# Отправка сообщения на модерацию ID
msgSendForm = "btn-write-plugin"
# Кнопка отправить CLASS_NAME
msgSendModerate = "btn-moderation-primary-send"
# Кнопка отмена CLASS_NAME
msdCancel = "btn-moderation-primary-close"
# Форма сообщения ID
msgForm = "plugin-message-textarea"
# Палец вверх ID
msgThumbUp = "btn-message-without-answer"
