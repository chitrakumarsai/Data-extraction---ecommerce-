require(rvest)
require(jsonlite)
require(dplyr)
require(foreach)
require(doParallel)
require(readr)
require(tictoc)
require(purrr)
require(furrr)
require(httr)

options(stringsAsFactors = F)


df_store_info <- read_csv('C:\\Users\\ChitraVenkata\\Desktop\\Walmart\\walmart_store_coordinates.csv')


#### Dog Treats & Chews ####

fn_scrape_dtc <- function(store, page){
  Sys.sleep(2.0)
  
  url_concat <- paste0(url_dtc1, 
                       '&page=', page,
                       '&offset=', (page - 1)*195,
                       '&count=', 200,
                       '&storeId=', store)
  
  json_dtc <- tryCatch(GET(url_concat, user_agent('Mozilla/5.0'),
                             add_headers(.headers = c(":authority" = "www.walmart.com",
                                                      ":method" = "GET",
                                                      ':scheme' = 'https',
                                                      'accept' = 'application/json, text/plain, */*',
                                                      'accept-encoding' = 'gzip, deflate, br',
                                                      'accept-language' = 'en-US, en;q=0.9',
                                                      'sec-fetch-dest' = 'document',
                                                      'sec-fetch-mode' = 'navigate',
                                                      'sec-fetch-site' = 'same-origin'))) %>% 
                         read_html() %>% 
                         html_text() %>% 
                         fromJSON(), error = function(e) 'Error: try again')
  
  list(json = json_dtc, store_id = store)
}


url_dtc1 <- 'https://grocery.walmart.com/v4/api/products/browse?taxonomyNodeId=1255027787121_1256653759776'


tic()

plan(cluster(workers = 2))
list_dtc1 <- df_store_info %>%  slice(1:100) %>% 
  pull(store_id) %>% 
  future_map(., ~fn_scrape_dtc(store = ., page = 1), .progress = T)
plan(sequential)


counter <- 1
while(counter < 5){
  for ( i in length(list_dtc1)){
    if (list_dtc1[[i]][['json']] == 'Error: try again'){
      fn_scrape_dtc(list_dtc1[[i]][['store_id']],1)
    }
    else if (list_dtc1[[i]][['json']] != 'Error: try again') {
      break
    }
  }
  counter =+ 1
}
toc()


## Create a data frame containing all combinations for store_id and page # that still need to be scraped
df_dtc_params <- list_dtc1 %>% 
  map(., 'json') %>% 
  map(., 'totalCount') %>% #number of items in the query
  as.character() %>% 
  data.frame(results = ., store_id = as.character(map(list_dtc1, 'store_id'))) %>% 
  mutate(., num_pages = ceiling(as.numeric(results) / 195)) %>% 
  filter(., num_pages > 1) %>%
  mutate(., page = 2) %>% 
  group_by(store_id) %>% 
  tidyr::complete(., page = seq(from = 2, to = num_pages)) %>% 
  ungroup() %>% 
  select(., store_id, page)


### Scrape Remaining DTC pages ###

tic()
plan(cluster(workers = 2))
list_dtc2 <- future_map2(.x = df_dtc_params$store_id, .y = df_dtc_params$page,
                        .f = ~fn_scrape_dtc(store = .x,
                                        page = .y),
                        .progress = T)
plan(sequential)
toc()



### Parse list to tabular data ###





item_id1 <- c(list_dtc1, list_dtc2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'USItemId')

# sku1 <- c(list_dtc1, list_dtc2) %>% 
#   map(., 'json') %>% 
#   map(., 'products') %>% 
#   map(., 'sku') %>% 
#   flatten() %>% 
#   as.character()

basic1 <- c(list_dtc1, list_dtc2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'basic')

basic1 <- lapply(basic1, function(x){ x["image"] <- NULL; x["adsMeta"] <- NULL; x["label"] <- NULL;x}) %>% 
  bind_rows()

detailed1 <- c(list_dtc1, list_dtc2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'detailed') %>% 
  bind_rows()

is_oos1 <- c(list_dtc1, list_dtc2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'store') %>% 
  map(., 'isOutOfStock') %>% 
  flatten() %>% 
  as.character()

price_info1 <- c(list_dtc1, list_dtc2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'store') %>% 
  map('price') %>% 
  bind_rows()

total_count1 <- c(list_dtc1, list_dtc2) %>% 
  map(., 'json') %>% 
  map(., 'totalCount') %>% 
  map2(.x = ., .y = item_id1, .f = ~rep(.x, length(.y))) %>% 
  flatten() %>% 
  as.character()

store_id1 <- c(list_dtc1, list_dtc2) %>% 
  map(., 'store_id') %>% 
  map2(.x = ., .y = item_id1, .f = ~rep(.x, length(.y))) %>% 
  flatten() %>% 
  as.character()

# category1 <- c(list_dtc1, list_dtc2) %>% 
#   map(., 'json') %>% 
#   map(., 'manualShelfName') %>% 
#   map2(.x = ., .y = item_id1, .f = ~rep(.x, length(.y))) %>% 
#   flatten() %>% 
#   as.character()

item_id1 <- item_id1 %>%
  flatten() %>%
  as.character()


df_dtc1 <- data.frame(store_id = store_id1,
                      item_id = item_id1,
                      # sku = sku1,
                      category = rep('Dog Treats & Chews', length(item_id1)),
                      is_oos = is_oos1,
                      total_count = total_count1,
                      basic1,
                      #detailed1,
                      price_info1)






#### Dog Supplies ####


fn_scrape_dog_sup <- function(store, page){
  Sys.sleep(1)
  
  url_concat <- paste0(url_dog_sup1, 
                       '&page=', page,
                       '&offset=', (page - 1)*195,
                       '&count=', 200,
                       '&storeId=', store)
  
  json_dog_sup <- tryCatch(GET(url_concat, user_agent('Mozilla/5.0'),
                               add_headers(.headers = c(":authority" = "www.walmart.com",
                                                        ":method" = "GET",
                                                        ':scheme' = 'https',
                                                        'accept' = 'application/json, text/plain, */*',
                                                        'accept-encoding' = 'gzip, deflate, br',
                                                        'accept-language' = 'en-US, en;q=0.9',
                                                        'sec-fetch-dest' = 'document',
                                                        'sec-fetch-mode' = 'navigate',
                                                        'sec-fetch-site' = 'same-origin'))) %>% 
                             read_html() %>% 
                             html_text() %>% 
                             fromJSON(), error = function(e) 'Error: try again')
  
  list(json = json_dog_sup, store_id = store)
}


url_dog_sup1 <- 'https://grocery.walmart.com/v4/api/products/browse?taxonomyNodeId=1255027787121_1256653759778'


tic()
plan(cluster(workers = 2))
list_dog_sup1 <- df_store_info %>%  slice(1:100) %>% 
  pull(store_id) %>% 
  future_map(., ~fn_scrape_dog_sup(store = ., page = 1), .progress = T)
plan(sequential)
toc()

tic()
counter <- 1
while(counter < 5){
  for ( i in length((list_dog_sup1))){
    if (list_dog_sup1[[i]][['json']] == 'Error: try again'){
      fn_scrape_dtc(list_dog_sup1[[i]][['store_id']],1)
    }
    counter =+ 1
    else {
      break
    }
  }
}
toc()


## Create a data frame containing all combinations for store_id and page # that still need to be scraped
df_dog_sup_params <- list_dog_sup1 %>% 
  map(., 'json') %>% 
  map(., 'totalCount') %>%
  as.character() %>% 
  data.frame(results = ., store_id = as.character(map(list_dog_sup1, 'store_id'))) %>% 
  mutate(., num_pages = ceiling(as.numeric(results) / 195)) %>% 
  filter(., num_pages > 1) %>%
  mutate(., page = 2) %>% 
  group_by(store_id) %>% 
  tidyr::complete(., page = seq(from = 2, to = num_pages)) %>% 
  ungroup() %>% 
  select(., store_id, page)


### Scrape Remaining Dog Supply pages ###
tic()
plan(cluster(workers = 2))
list_dog_sup2 <- future_map2(.x = df_dog_sup_params$store_id, .y = df_dog_sup_params$page,
                             .f = ~fn_scrape_dog_sup(store = .x, page = .y),
                             .progress = T)
plan(sequential)
toc()


### Parse Dog Supply JSON ###




item_id1 <- c(list_dog_sup1, list_dog_sup2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'USItemId')

# sku1 <- c(list_dog_sup1, list_dog_sup2) %>% 
#   map(., 'json') %>% 
#   map(., 'products') %>% 
#   map(., 'sku') %>% 
#   flatten() %>% 
#   as.character()

basic1 <- c(list_dog_sup1, list_dog_sup2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'basic')

basic1 <- lapply(basic1, function(x){ x["image"] <- NULL; x["adsMeta"] <- NULL; x["label"] <- NULL;x}) %>% 
  bind_rows()

detailed1 <- c(list_dog_sup1, list_dog_sup2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'detailed') %>% 
  bind_rows()

is_oos1 <- c(list_dog_sup1, list_dog_sup2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'store') %>% 
  map(., 'isOutOfStock') %>% 
  flatten() %>% 
  as.character()

price_info1 <- c(list_dog_sup1, list_dog_sup2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'store') %>% 
  map('price') %>% 
  bind_rows()

total_count1 <- c(list_dog_sup1, list_dog_sup2) %>% 
  map(., 'json') %>% 
  map(., 'totalCount') %>% 
  map2(.x = ., .y = item_id1, .f = ~rep(.x, length(.y))) %>% 
  flatten() %>% 
  as.character()

store_id1 <- c(list_dog_sup1, list_dog_sup2) %>% 
  map(., 'store_id') %>% 
  map2(.x = ., .y = item_id1, .f = ~rep(.x, length(.y))) %>% 
  flatten() %>% 
  as.character()

# category1 <- c(list_dog_sup1, list_dog_sup2) %>% 
#   map(., 'json') %>% 
#   map(., 'filters') %>% 
#   map(., 'categories') %>% 
#   map(., 'values') %>% 
#   flatten() %>% 
#   map(., 'name') %>% 
#   .[[1]] %>% 
#   rep(., length = length(store_id1))

item_id1 <- item_id1 %>% 
  flatten() %>% 
  as.character()


df_dog_sup1 <- data.frame(store_id = store_id1,
                          item_id = item_id1,
                          # sku = sku1,
                          category = rep('Dog Supplies', length(item_id1)),
                          is_oos = is_oos1,
                          total_count = total_count1,
                          basic1,
                         # detailed1,
                          price_info1)



#### CAT FOOD ####

# 
# fn_scrape_cat_food <- function(store, page){
#   Sys.sleep(0.5)
#   
#   url_concat <- paste0(url_cat_food1, 
#                        '&page=', page,
#                        '&offset=', (page - 1)*120,
#                        '&count=', 120,
#                        '&storeId=', store)
#   
#   json_cat_food <- tryCatch(read_html(url_concat) %>% 
#                               html_text() %>% 
#                               fromJSON(), error = function(e) 'Error: try again')
#   
#   list(json = json_cat_food, store_id = store)
# }
# 
# 
# url_cat_food1 <- 'https://grocery.walmart.com/v4/api/products/browse?taxonomyNodeId=1255027787121_1255027787461'
# 
# 
# tic()
# plan(multisession)
# list_cat_food1 <- df_store_info %>% 
#   pull(store_id) %>% 
#   future_map(., ~fn_scrape_cat_food(store = ., page = 1), .progress = T)
# plan(sequential)
# toc()
# 
# 
# ## Create a data frame containing all combinations for store_id and page # that still need to be scraped
# df_cat_food_params <- list_cat_food1 %>% 
#   map(., 'json') %>% 
#   map(., 'totalCount') %>%
#   as.character() %>% 
#   data.frame(results = ., store_id = as.character(map(list_cat_food1, 'store_id'))) %>% 
#   mutate(., num_pages = ceiling(as.numeric(results) / 120)) %>% 
#   filter(., num_pages > 1) %>%
#   mutate(., page = 2) %>% 
#   group_by(store_id) %>% 
#   tidyr::complete(., page = seq(from = 2, to = num_pages)) %>% 
#   ungroup() %>% 
#   select(., store_id, page)
# 
# 
# ### Scrape Remaining CAT FOOD pages ###
# tic()
# plan(multisession)
# list_cat_food2 <- future_map2(.x = df_cat_food_params$store_id, .y = df_cat_food_params$page,
#                               .f = ~fn_scrape_cat_food(store = .x, page = .y),
#                               .progress = T)
# plan(sequential)
# toc()
# 
# 
# ### Parse CAT FOOD JSON ###
# 
# 
# 
# item_id1 <- c(list_cat_food1, list_cat_food2) %>% 
#   map(., 'json') %>% 
#   map(., 'products') %>% 
#   map(., 'USItemId')
# 
# # sku1 <- c(list_cat_food1, list_cat_food2) %>% 
# #   map(., 'json') %>% 
# #   map(., 'products') %>% 
# #   map(., 'sku') %>% 
# #   flatten() %>% 
# #   as.character()
# 
# basic1 <- c(list_cat_food1, list_cat_food2) %>% 
#   map(., 'json') %>% 
#   map(., 'products') %>% 
#   map(., 'basic')
# 
# basic1 <- lapply(basic1, function(x){ x["image"] <- NULL; x}) %>% 
#   bind_rows()
# 
# detailed1 <- c(list_cat_food1, list_cat_food2) %>% 
#   map(., 'json') %>% 
#   map(., 'products') %>% 
#   map(., 'detailed') %>% 
#   bind_rows()
# 
# is_oos1 <- c(list_cat_food1, list_cat_food2) %>% 
#   map(., 'json') %>% 
#   map(., 'products') %>% 
#   map(., 'store') %>% 
#   map(., 'isOutOfStock') %>% 
#   flatten() %>% 
#   as.character()
# 
# price_info1 <- c(list_cat_food1, list_cat_food2) %>% 
#   map(., 'json') %>% 
#   map(., 'products') %>% 
#   map(., 'store') %>% 
#   map('price') %>% 
#   bind_rows()
# 
# total_count1 <- c(list_cat_food1, list_cat_food2) %>% 
#   map(., 'json') %>% 
#   map(., 'totalCount') %>% 
#   map2(.x = ., .y = item_id1, .f = ~rep(.x, length(.y))) %>% 
#   flatten() %>% 
#   as.character()
# 
# store_id1 <- c(list_cat_food1, list_cat_food2) %>% 
#   map(., 'store_id') %>% 
#   map2(.x = ., .y = item_id1, .f = ~rep(.x, length(.y))) %>% 
#   flatten() %>% 
#   as.character()
# 
# category1 <- c(list_cat_food1, list_cat_food2) %>% 
#   map(., 'json') %>% 
#   map(., 'manualShelfName') %>% 
#   map2(.x = ., .y = item_id1, .f = ~rep(.x, length(.y))) %>% 
#   flatten() %>% 
#   as.character()
# 
# item_id1 <- item_id1 %>% 
#   flatten() %>% 
#   as.character()
# 
# 
# df_cat_food1 <- data.frame(store_id = store_id1,
#                            item_id = item_id1,
#                            # sku = sku1,
#                            category = category1,
#                            is_oos = is_oos1,
#                            total_count = total_count1,
#                            basic1,
#                            detailed1,
#                            price_info1)
# 




#### CAT TREATS ####


fn_scrape_cat_treats <- function(store, page){
  Sys.sleep(1)
  
  url_concat <- paste0(url_cat_treats1, 
                       '&page=', page,
                       '&offset=', (page - 1)*195,
                       '&count=', 200,
                       '&storeId=', store)
  
  json_cat_treats <- tryCatch(GET(url_concat, user_agent('Mozilla/5.0'),
                                  add_headers(.headers = c(":authority" = "www.walmart.com",
                                                           ":method" = "GET",
                                                           ':scheme' = 'https',
                                                           'accept' = 'application/json, text/plain, */*',
                                                           'accept-encoding' = 'gzip, deflate, br',
                                                           'accept-language' = 'en-US, en;q=0.9',
                                                           'sec-fetch-dest' = 'document',
                                                           'sec-fetch-mode' = 'navigate',
                                                           'sec-fetch-site' = 'same-origin'))) %>% 
                                read_html() %>% 
                                html_text() %>% 
                                fromJSON(), error = function(e) 'Error: try again')
  
  list(json = json_cat_treats, store_id = store)
}


url_cat_treats1 <- 'https://grocery.walmart.com/v4/api/products/browse?taxonomyNodeId=1255027787121_1256653759780'


tic()
plan(cluster(workers = 2))
list_cat_treats1 <- df_store_info %>% 
  pull(store_id) %>% 
  future_map(., ~fn_scrape_cat_treats(store = ., page = 1), .progress = T)
plan(sequential)
toc()


## Create a data frame containing all combinations for store_id and page # that still need to be scraped
# df_cat_treats_params <- list_cat_treats1 %>% 
#   map(., 'json') %>% 
#   map(., 'totalCount') %>%
#   as.character() %>% 
#   data.frame(results = ., store_id = as.character(map(list_cat_treats1, 'store_id'))) %>% 
#   mutate(., num_pages = ceiling(as.numeric(results) / 195)) %>% 
#   filter(., num_pages > 1) %>%
#   mutate(., page = 2) %>% 
#   group_by(store_id) %>% 
#   tidyr::complete(., page = seq(from = 2, to = num_pages)) %>% 
#   ungroup() %>% 
#   select(., store_id, page)


### Scrape Remaining CAT FOOD pages ###
# tic()
# plan(multisession)
# list_cat_treats2 <- future_map2(.x = df_cat_treats_params$store_id, .y = df_cat_treats_params$page,
#                                 .f = ~fn_scrape_cat_treats(store = .x, page = .y),
#                                 .progress = T)
# plan(sequential)
# toc()


### Parse CAT FOOD JSON ###



item_id1 <- c(list_cat_treats1) %>% #, list_cat_treats2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'USItemId')

# sku1 <- c(list_cat_treats1, list_cat_treats2) %>% 
#   map(., 'json') %>% 
#   map(., 'products') %>% 
#   map(., 'sku') %>% 
#   flatten() %>% 
#   as.character()

basic1 <- c(list_cat_treats1) %>% #, list_cat_treats2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'basic')

basic1 <- lapply(basic1, function(x){ x["image"] <- NULL; x}) %>% 
  bind_rows()

detailed1 <- c(list_cat_treats1) %>% #, list_cat_treats2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'detailed') %>% 
  bind_rows()


is_oos1 <- c(list_cat_treats1) %>% #, list_cat_treats2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'store') %>% 
  map(., 'isOutOfStock') %>% 
  flatten() %>% 
  as.character()

price_info1 <- c(list_cat_treats1) %>% #, list_cat_treats2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'store') %>% 
  map('price') %>% 
  bind_rows()

total_count1 <- c(list_cat_treats1) %>% #, list_cat_treats2) %>% 
  map(., 'json') %>% 
  map(., 'totalCount') %>% 
  map2(.x = ., .y = item_id1, .f = ~rep(.x, length(.y))) %>% 
  flatten() %>% 
  as.character()

store_id1 <- c(list_cat_treats1) %>% #, list_cat_treats2) %>% 
  map(., 'store_id') %>% 
  map2(.x = ., .y = item_id1, .f = ~rep(.x, length(.y))) %>% 
  flatten() %>% 
  as.character()

# category1 <- c(list_cat_treats1, list_cat_treats2) %>% 
#   map(., 'json') %>% 
#   map(., 'manualShelfName') %>% 
#   map2(.x = ., .y = item_id1, .f = ~rep(.x, length(.y))) %>% 
#   flatten() %>% 
#   as.character()

item_id1 <- item_id1 %>% 
  flatten() %>% 
  as.character()


if(nrow(detailed1) != length(item_id1)){
  detailed1 <- data.frame(rating = rep(NA, length(item_id1)),
                          reviewsCount = rep(NA, length(item_id1)))
}





df_cat_treats1 <- data.frame(store_id = store_id1,
                             item_id = item_id1,
                             # sku = sku1,
                             category = rep('Cat Treats', length(item_id1)),
                             is_oos = is_oos1,
                             total_count = total_count1,
                             basic1,
                            detailed1,
                             price_info1)




#### CAT Litter & Accessories ####


fn_scrape_cat_lit_accs <- function(store, page){
  Sys.sleep(1)
  
  url_concat <- paste0(url_cat_lit_accs1, 
                       '&page=', page,
                       '&offset=', (page - 1)*195,
                       '&count=', 200,
                       '&storeId=', store)
  
  json_cat_lit_accs <- tryCatch(GET(url_concat, user_agent('Mozilla/5.0')) %>% 
                                  read_html() %>% 
                                  html_text() %>% 
                                  fromJSON(), error = function(e) 'Error: try again')
  
  list(json = json_cat_lit_accs, store_id = store)
}


url_cat_lit_accs1 <- 'https://grocery.walmart.com/v4/api/products/browse?taxonomyNodeId=1255027787121_1256653759782'


tic()
plan(multisession)
list_cat_lit_accs1 <- df_store_info %>% 
  pull(store_id) %>% 
  future_map(., ~fn_scrape_cat_lit_accs(store = ., page = 1), .progress = T)
plan(sequential)
toc()


## Create a data frame containing all combinations for store_id and page # that still need to be scraped
# df_cat_lit_accs_params <- list_cat_lit_accs1 %>% 
#   map(., 'json') %>% 
#   map(., 'totalCount') %>%
#   as.character() %>% 
#   data.frame(results = ., store_id = as.character(map(list_cat_lit_accs1, 'store_id'))) %>% 
#   mutate(., num_pages = ceiling(as.numeric(results) / 195)) %>% 
#   filter(., num_pages > 1) %>%
#   mutate(., page = 2) %>% 
#   group_by(store_id) %>% 
#   tidyr::complete(., page = seq(from = 2, to = num_pages)) %>% 
#   ungroup() %>% 
#   select(., store_id, page)


### Scrape Remaining CAT FOOD pages ###
# tic()
# plan(multisession)
# list_cat_lit_accs2 <- tryCatch(future_map2(.x = df_cat_lit_accs_params$store_id, .y = df_cat_lit_accs_params$page,
#                                   .f = ~fn_scrape_cat_lit_accs(store = .x, page = .y),
#                                   .progress = T), error = function(e) NULL)
# plan(sequential)
# toc()
# 

### Parse CAT Litter Accessories ###



item_id1 <- c(list_cat_lit_accs1) %>% #, list_cat_lit_accs2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'USItemId')

# sku1 <- c(list_cat_lit_accs1, list_cat_lit_accs2) %>% 
#   map(., 'json') %>% 
#   map(., 'products') %>% 
#   map(., 'sku') %>% 
#   flatten() %>% 
#   as.character()

basic1 <- c(list_cat_lit_accs1) %>% #, list_cat_lit_accs2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'basic')

basic1 <- lapply(basic1, function(x){ x["image"] <- NULL; x}) %>% 
  bind_rows()

detailed1 <- c(list_cat_lit_accs1) %>% #, list_cat_lit_accs2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'detailed') %>% 
  bind_rows()

is_oos1 <- c(list_cat_lit_accs1) %>% #, list_cat_lit_accs2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'store') %>% 
  map(., 'isOutOfStock') %>% 
  flatten() %>% 
  as.character()

price_info1 <- c(list_cat_lit_accs1) %>% #, list_cat_lit_accs2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'store') %>% 
  map('price') %>% 
  bind_rows()

total_count1 <- c(list_cat_lit_accs1) %>% #, list_cat_lit_accs2) %>% 
  map(., 'json') %>% 
  map(., 'totalCount') %>% 
  map2(.x = ., .y = item_id1, .f = ~rep(.x, length(.y))) %>% 
  flatten() %>% 
  as.character()

store_id1 <- c(list_cat_lit_accs1) %>% #, list_cat_lit_accs2) %>% 
  map(., 'store_id') %>% 
  map2(.x = ., .y = item_id1, .f = ~rep(.x, length(.y))) %>% 
  flatten() %>% 
  as.character()

# category1 <- c(list_cat_lit_accs1) %>% #, list_cat_lit_accs2) %>% 
#   map(., 'json') %>% 
#   map(., 'manualShelfName') %>% 
#   map2(.x = ., .y = item_id1, .f = ~rep(.x, length(.y))) %>% 
#   flatten() %>% 
#   as.character()

item_id1 <- item_id1 %>% 
  flatten() %>% 
  as.character()


df_cat_lit_accs1 <- data.frame(store_id = store_id1,
                               item_id = item_id1,
                               # sku = sku1,
                               category = rep('Cat Litter & Accessories', length(item_id1)),
                               is_oos = is_oos1,
                               total_count = total_count1,
                               basic1,
                               detailed1,
                               price_info1)




#### CAT SUPPLIES ####


fn_scrape_cat_sups <- function(store, page){
  Sys.sleep(1)
  
  url_concat <- paste0(url_cat_sups1, 
                       '&page=', page,
                       '&offset=', (page - 1)*195,
                       '&count=', 200,
                       '&storeId=', store)
  
  json_cat_sups <- tryCatch(GET(url_concat, user_agent('Mozilla/5.0')) %>% 
                              read_html() %>% 
                              html_text() %>% 
                              fromJSON(), error = function(e) 'Error: try again')
  
  list(json = json_cat_sups, store_id = store)
}


url_cat_sups1 <- 'https://grocery.walmart.com/v4/api/products/browse?taxonomyNodeId=1255027787121_1256653759784'


tic()
plan(multisession)
list_cat_sups1 <- df_store_info %>% 
  pull(store_id) %>% 
  future_map(., ~fn_scrape_cat_sups(store = ., page = 1), .progress = T)
plan(sequential)
toc()


## Create a data frame containing all combinations for store_id and page # that still need to be scraped
# df_cat_sups_params <- list_cat_sups1 %>% 
#   map(., 'json') %>% 
#   map(., 'totalCount') %>%
#   as.character() %>% 
#   data.frame(results = ., store_id = as.character(map(list_cat_sups1, 'store_id'))) %>% 
#   mutate(., num_pages = ceiling(as.numeric(results) / 195)) %>% 
#   filter(., num_pages > 1) %>%
#   mutate(., page = 2) %>% 
#   group_by(store_id) %>% 
#   tidyr::complete(., page = seq(from = 2, to = num_pages)) %>% 
#   ungroup() %>% 
#   select(., store_id, page)


### Scrape Remaining CAT FOOD pages ###
# tic()
# plan(multisession)
# list_cat_sups2 <- future_map2(.x = df_cat_sups_params$store_id, .y = df_cat_sups_params$page,
#                               .f = ~fn_scrape_cat_sups(store = .x, page = .y),
#                               .progress = T)
# plan(sequential)
# toc()


### Parse CAT FOOD JSON ###



item_id1 <- c(list_cat_sups1) %>% #, list_cat_sups2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'USItemId')

# sku1 <- c(list_cat_sups1, list_cat_sups2) %>% 
#   map(., 'json') %>% 
#   map(., 'products') %>% 
#   map(., 'sku') %>% 
#   flatten() %>% 
#   as.character()

basic1 <- c(list_cat_sups1) %>% #, list_cat_sups2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'basic')

basic1 <- lapply(basic1, function(x){ x["image"] <- NULL; x}) %>% 
  bind_rows()

detailed1 <- c(list_cat_sups1) %>% #, list_cat_sups2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'detailed') %>% 
  bind_rows()

is_oos1 <- c(list_cat_sups1) %>% #, list_cat_sups2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'store') %>% 
  map(., 'isOutOfStock') %>% 
  flatten() %>% 
  as.character()

price_info1 <- c(list_cat_sups1) %>% #, list_cat_sups2) %>% 
  map(., 'json') %>% 
  map(., 'products') %>% 
  map(., 'store') %>% 
  map('price') %>% 
  bind_rows()

total_count1 <- c(list_cat_sups1) %>% #, list_cat_sups2) %>% 
  map(., 'json') %>% 
  map(., 'totalCount') %>% 
  map2(.x = ., .y = item_id1, .f = ~rep(.x, length(.y))) %>% 
  flatten() %>% 
  as.character()

store_id1 <- c(list_cat_sups1) %>% #, list_cat_sups2) %>% 
  map(., 'store_id') %>% 
  map2(.x = ., .y = item_id1, .f = ~rep(.x, length(.y))) %>% 
  flatten() %>% 
  as.character()
# 
# category1 <- c(list_cat_sups1) %>% #, list_cat_sups2) %>% 
#   map(., 'json') %>% 
#   map(., 'manualShelfName') %>% 
#   map2(.x = ., .y = item_id1, .f = ~rep(.x, length(.y))) %>% 
#   flatten() %>% 
#   as.character()

item_id1 <- item_id1 %>% 
  flatten() %>% 
  as.character()


if(nrow(detailed1) != length(item_id1)){
  detailed1 <- data.frame(rating = rep(NA, length(item_id1)),
                          reviewsCount = rep(NA, length(item_id1)))
}


df_cat_sups1 <- data.frame(store_id = store_id1,
                           item_id = item_id1,
                           # sku = sku1,
                           category = rep('Cat Supplies', length(item_id1)),
                           is_oos = is_oos1,
                           total_count = total_count1,
                           basic1,
                           detailed1,
                           price_info1)





#### Aggregate all data frames ####



df_pet_agg <- bind_rows(df_cat_lit_accs1,
                        df_cat_sups1,
                        df_cat_treats1,
                        df_dog_sup1,
                        df_dtc1) %>% 
  left_join(., mutate_all(rename(df_store_info, store_name = name), as.character), by = 'store_id') %>% 
  select(., -adsMeta) %>% 
  distinct(., store_id, item_id, .keep_all = T)




tic()
write_csv(df_pet_agg,
          path = paste0('C:/Users/ChitraVenkata/Desktop//Walmart/pet_dept_store_lvl_',
                 Sys.Date(),
                 '.csv'))
toc()




#### Code Bank ####

# tic()
# registerDoParallel(cores = 12)
# list_dtc1 <- foreach(i = df_store_info$store_id, .packages = c("jsonlite", "rvest", "dplyr")) %dopar% {
#   Sys.sleep(0.5)
#   
#   url_concat <- paste0(url_dtc1, 
#                        '&page=', 1,
#                        '&offset=', 0,
#                        '&count=', 200,
#                        '&storeId=', i)
#   
#   json_dtc <- read_html(url_concat) %>% 
#   html_text() %>% 
#   fromJSON()
#   
#   # item_id <- json_dtc$products$USItemId
#   # sku <- json_dtc$products$sku
#   # basic <- json_dtc[['products']][['basic']] %>% select(., -image)
#   # detailed <- json_dtc[['products']][['detailed']]
#   # is_oos <- json_dtc[['products']][['store']]$isOutOfStock
#   # price_info <- json_dtc[['products']][['store']][['price']]
#   # total_count <- rep(json_dtc$totalCount, length(item_id))
#   
#   list(json = json_dtc, store_id = i)
#   
# }
# stopImplicitCluster()
# toc()







