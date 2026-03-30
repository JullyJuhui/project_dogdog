**'네이밍 컨벤션(Naming Convention) 최적화'**

### 🗂️ 1. 테이블명 (Table Names) 개선 추천

| 도메인 | 현재 테이블명 (Current) | 추천 1 (Best) | 추천 2 | 추천 3 |
| :--- | :--- | :--- | :--- | :--- |
| **Common** | **customer** | 유지 (customer) |  |  |
| | `customer_status` | `customer_detail` | **customer_info** |  |
| **Companion** | `butler` | **pet_owner** |  |  |
| | `pet` | **유지 (pet)** |  |  |
| | `pet_log_boolean` | **pet_health_check** | `pet_daily_log` | `pet_status_flag` |
| | `pet_log_numeric` | **pet_vital_log** | `pet_metric` | `pet_health_metric` |
| | `pet_feeding_suggest` | **feeding_guide** | `pet_diet_plan` | `suggested_feeding` |
| | `breed` | **유지 (breed)** | `pet_breed` | `species` |
| | `pet_food` | **feeding_log** | `pet_meal_log` | `food_record` |
| | `pet_food_subscribe` | **pet_subscription** | `food_subscription` | `pet_sub_log` |
| | `breed_life` | **life_stage** | `breed_stage` | `age_stage` |
| **ERP** | `employees` | **employee** (단수 통일) | `staff` | `admin_user` |
| | `emp_position` | **position** | `job_title` | `employee_role` |
| | `attendance` | **유지 (attendance)** | `work_log` | `timesheet` |
| | `purchasing` | **purchase_order** | `purchase` | `supply_order` |
| | `purchasing_list` | **purchase_item** | `purchase_detail` | `po_line` |
| | `inbound` | **유지 (inbound)** | `receiving` | `stock_in` |
| | `Inventory` | **inventory** (소문자) | `stock` | `warehouse_stock` |
| | `storage_status` | **inbound_status** | `stock_status` | `warehouse_status` |
| | `supplier` | **유지 (supplier)** | `vendor` | `partner` |
| **OPD** | `financial_company` | **payment_provider** | `finance_corp` | `card_company` |
| | `payment_billing` | **billing_key** | `payment_method` | `user_card` |
| | `product` | **유지 (product)** | `item` | `goods` |
| | `product_status` | **product_detail** | `product_info` | `product_meta` |
| | `product_type` | **product_category** | `item_type` | `goods_type` |
| | `customer_wish_list` | **wishlist** | `wish_item` | `user_wishlist` |
| | `customer_cart` | **cart** | `cart_item` | `user_cart` |
| | `orders` | **order_info** | `orders` (유지) | `purchase_order` |
| | `orders_product_list` | **order_item** | `order_detail` | `order_line` |
| | `payment` | **유지 (payment)** | `transaction` | `order_payment` |
| | `payment_status` | **유지 (payment_status)** | `pay_status` | `transaction_status` |
| | `delivery` | **유지 (delivery)** | `shipment` | `shipping` |
| | `delivery_return` | **return_order** | `refund` | `claim` |
| | `delivery_return_product_list`| **return_item** | `return_detail` | `refund_item` |
| | `delivery_status` | **유지 (delivery_status)** | `shipping_status` | `shipment_status` |
| **Subscribe** | `subscribe_plan` | **유지 (subscribe_plan)** | `sub_plan` | `plan` |
| | `subscribe` | **subscription** | `sub_order` | `subscribe_master` |
| | `subscribe_status` | **subscribe_detail** | `subscribe_info` | `subscribe_delivery` |
| | `subscribe_product` | **subscribe_item** | `subscribe_detail` | `sub_product` |

---

### 🏷️ 2. 컬럼명 (Column Names) 개선 추천

#### 🐾 Companion & Customer 도메인
| 현재 컬럼명 (Current) | 추천 1 (Best) | 추천 2 | 추천 3 |
| :--- | :--- | :--- | :--- |
| `customer.subscribe` | **is_subscribed** | `has_subscription` | `sub_status` |
| `customer_status.auth` | **auth_provider** | `sns_type` | `login_type` |
| `customer_status.auth_api` | **provider_id** | `oauth_token` | `sns_id` |
| `pet.breed_id` | **유지 (breed_id)** | `species_id` | `pet_breed_id` |
| `pet.sex` | **gender** | `sex` (유지) | `is_male` |
| `pet.neutering` | **is_neutered** | `has_neutered` | `neutering` (유지) |
| `pet.walking` | **walk_frequency** | `daily_walks` | `walking_count` |
| `pet.feeding` | **feed_frequency** | `daily_meals` | `feeding_count` |
| `pet.supps` | **supplements** | `supps_memo` | `vitamins` |
| `butler.main_butler` | **is_main** | `is_primary` | `main_owner` |
| `butler.pet_profile_photo` | **profile_image** | `avatar_url` | `profile_photo` |
| `pet_log_boolean.status_boolean`| **is_done** | `status` | `check_result` |
| `pet_log_numeric.status_numeric`| **metric_value** | `value` | `measure_val` |
| `pet_food_subscribe.remineder` | **reminder** (오타수정) | `remaining_count` | `left_qty` |

#### 🏢 ERP (인사/물류) 도메인
| 현재 컬럼명 (Current) | 추천 1 (Best) | 추천 2 | 추천 3 |
| :--- | :--- | :--- | :--- |
| `employees.emp` (아이디) | **username** | `login_id` | `account_id` |
| `employees.name` | **emp_name** | `full_name` | `name` (유지) |
| `employee.emp_id_photo` | **profile_image** | `id_photo` | `photo_url` |
| `attendance.etc` | **memo** | `remark` | `note` |
| `purchasing.payment_status` | **pay_status** | `is_paid` | `settlement_status` |
| `purchasing_list.all_amount` | **unit_price** | `supply_price` | `base_amount` |
| `purchasing_list.total_amount` | **total_price** | `sum_amount` | `net_total` |
| `inventory.save_stock` | **total_stock** | `inbound_qty` | `base_stock` |
| `inventory.scrap_stock` | **defective_stock** | `loss_qty` | `scrap_qty` |
| `supplier.contact_status` | **is_active** | `is_contracted` | `status` |
| `supplier.sup_manager` | **manager_name** | `pic_name` (Person In Charge)| `contact_person` |

#### 🛒 OPD (주문/상품/배송) 도메인
| 현재 컬럼명 (Current) | 추천 1 (Best) | 추천 2 | 추천 3 |
| :--- | :--- | :--- | :--- |
| `payment_billing.default_card` | **is_default** | `is_primary` | `main_card` |
| `product.product` | **product_name** | `name` | `item_name` |
| `product.embed` | **embedding** | `vector_data` | `ai_embed` |
| `product.tag` | **tags** | `search_tags` | `keywords` |
| `product_status.protein` | **protein_type** | `is_animal_protein`| `base_protein` |
| `product_status.classification` | **is_sample** | `is_trial` | `sample_flag` |
| `orders_product_list.amount` | **unit_price** | `price` | `sale_price` |
| `payment.option` | **installment_months**| `installment` | `pay_option` |
| `payment.cancel` | **is_canceled** | `is_refunded` | `cancel_flag` |
| `delivery.invoice` | **tracking_number** | `waybill_no` | `invoice_no` |
| `delivery_return.all_non_refundable`| **is_all_defective**| `is_total_loss` | `all_damaged` |
| `delivery_return_product_list.customer_return_meno`| **return_memo** (오타수정) | `customer_memo` | `reason_memo` |

#### 🔁 Subscribe (정기구독) 도메인
| 현재 컬럼명 (Current) | 추천 1 (Best) | 추천 2 | 추천 3 |
| :--- | :--- | :--- | :--- |
| `subscribe.subscribe_status` | **status** | `sub_state` | `state` |
| `subscribe_status.food_stock_auto_delivery`| **auto_delivery** | `is_auto_ship` | `smart_delivery` |
| `subscribe_product.amount` | **unit_price** | `base_price` | `price` |
| `subscribe_product.sale_total_amount`| **discounted_total**| `final_price` | `pay_amount` |

---

### 💡 (참고) 공통적으로 적용된 네이밍 규칙
1. **PK/FK 이름은 유지:** `customer_id`, `product_id` 처럼 `테이블명_id` 규칙은 아주 잘 작성되어 있어 모두 그대로 유지했습니다.
2. **Boolean 통일:** 참/거짓을 나타내는 컬럼(`subscribe`, `neutering`, `cancel`)은 앞에 `is_`를 붙여 직관적으로 만들었습니다.
3. **금액/수량 명확화:** `amount`가 단가인지 총액인지 헷갈릴 수 있는 부분을 `unit_price`, `total_price` 등으로 명확히 분리했습니다.
4. **중복 단어 제거:** `product` 테이블의 `product` 컬럼처럼 테이블명과 컬럼명이 같은 경우 `product_name`으로 구체화했습니다