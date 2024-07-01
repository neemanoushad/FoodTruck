-- phpMyAdmin SQL Dump
-- version 4.1.6
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 17, 2024 at 12:34 PM
-- Server version: 5.6.16
-- PHP Version: 5.5.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `foodtruckdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=81 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add assigntbl', 7, 'add_assigntbl'),
(26, 'Can change assigntbl', 7, 'change_assigntbl'),
(27, 'Can delete assigntbl', 7, 'delete_assigntbl'),
(28, 'Can view assigntbl', 7, 'view_assigntbl'),
(29, 'Can add cartitems', 8, 'add_cartitems'),
(30, 'Can change cartitems', 8, 'change_cartitems'),
(31, 'Can delete cartitems', 8, 'delete_cartitems'),
(32, 'Can view cartitems', 8, 'view_cartitems'),
(33, 'Can add categorytbl', 9, 'add_categorytbl'),
(34, 'Can change categorytbl', 9, 'change_categorytbl'),
(35, 'Can delete categorytbl', 9, 'delete_categorytbl'),
(36, 'Can view categorytbl', 9, 'view_categorytbl'),
(37, 'Can add charitytbl', 10, 'add_charitytbl'),
(38, 'Can change charitytbl', 10, 'change_charitytbl'),
(39, 'Can delete charitytbl', 10, 'delete_charitytbl'),
(40, 'Can view charitytbl', 10, 'view_charitytbl'),
(41, 'Can add complainttbl', 11, 'add_complainttbl'),
(42, 'Can change complainttbl', 11, 'change_complainttbl'),
(43, 'Can delete complainttbl', 11, 'delete_complainttbl'),
(44, 'Can view complainttbl', 11, 'view_complainttbl'),
(45, 'Can add delivertbl', 12, 'add_delivertbl'),
(46, 'Can change delivertbl', 12, 'change_delivertbl'),
(47, 'Can delete delivertbl', 12, 'delete_delivertbl'),
(48, 'Can view delivertbl', 12, 'view_delivertbl'),
(49, 'Can add feedbacktbl', 13, 'add_feedbacktbl'),
(50, 'Can change feedbacktbl', 13, 'change_feedbacktbl'),
(51, 'Can delete feedbacktbl', 13, 'delete_feedbacktbl'),
(52, 'Can view feedbacktbl', 13, 'view_feedbacktbl'),
(53, 'Can add foodreqtbl', 14, 'add_foodreqtbl'),
(54, 'Can change foodreqtbl', 14, 'change_foodreqtbl'),
(55, 'Can delete foodreqtbl', 14, 'delete_foodreqtbl'),
(56, 'Can view foodreqtbl', 14, 'view_foodreqtbl'),
(57, 'Can add foodtbl', 15, 'add_foodtbl'),
(58, 'Can change foodtbl', 15, 'change_foodtbl'),
(59, 'Can delete foodtbl', 15, 'delete_foodtbl'),
(60, 'Can view foodtbl', 15, 'view_foodtbl'),
(61, 'Can add products', 16, 'add_products'),
(62, 'Can change products', 16, 'change_products'),
(63, 'Can delete products', 16, 'delete_products'),
(64, 'Can view products', 16, 'view_products'),
(65, 'Can add purchases', 17, 'add_purchases'),
(66, 'Can change purchases', 17, 'change_purchases'),
(67, 'Can delete purchases', 17, 'delete_purchases'),
(68, 'Can view purchases', 17, 'view_purchases'),
(69, 'Can add rewardtbl', 18, 'add_rewardtbl'),
(70, 'Can change rewardtbl', 18, 'change_rewardtbl'),
(71, 'Can delete rewardtbl', 18, 'delete_rewardtbl'),
(72, 'Can view rewardtbl', 18, 'view_rewardtbl'),
(73, 'Can add trucktbl', 19, 'add_trucktbl'),
(74, 'Can change trucktbl', 19, 'change_trucktbl'),
(75, 'Can delete trucktbl', 19, 'delete_trucktbl'),
(76, 'Can view trucktbl', 19, 'view_trucktbl'),
(77, 'Can add userregtbl', 20, 'add_userregtbl'),
(78, 'Can change userregtbl', 20, 'change_userregtbl'),
(79, 'Can delete userregtbl', 20, 'delete_userregtbl'),
(80, 'Can view userregtbl', 20, 'view_userregtbl');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=21 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'foodtruck', 'assigntbl'),
(8, 'foodtruck', 'cartitems'),
(9, 'foodtruck', 'categorytbl'),
(10, 'foodtruck', 'charitytbl'),
(11, 'foodtruck', 'complainttbl'),
(12, 'foodtruck', 'delivertbl'),
(13, 'foodtruck', 'feedbacktbl'),
(14, 'foodtruck', 'foodreqtbl'),
(15, 'foodtruck', 'foodtbl'),
(16, 'foodtruck', 'products'),
(17, 'foodtruck', 'purchases'),
(18, 'foodtruck', 'rewardtbl'),
(19, 'foodtruck', 'trucktbl'),
(20, 'foodtruck', 'userregtbl'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=21 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-03-26 07:35:22.571187'),
(2, 'auth', '0001_initial', '2024-03-26 07:35:40.313733'),
(3, 'admin', '0001_initial', '2024-03-26 07:35:46.796942'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-03-26 07:35:46.856507'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-03-26 07:35:46.922236'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-03-26 07:35:49.869523'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-03-26 07:35:51.656134'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-03-26 07:35:53.600571'),
(9, 'auth', '0004_alter_user_username_opts', '2024-03-26 07:35:53.667106'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-03-26 07:35:54.997484'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-03-26 07:35:55.067146'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-03-26 07:35:55.139434'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-03-26 07:35:56.751750'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-03-26 07:35:58.174352'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-03-26 07:36:01.126588'),
(16, 'auth', '0011_update_proxy_permissions', '2024-03-26 07:36:01.225404'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-03-26 07:36:02.507051'),
(18, 'foodtruck', '0001_initial', '2024-03-26 07:36:16.916434'),
(19, 'sessions', '0001_initial', '2024-03-26 07:36:18.814279'),
(20, 'foodtruck', '0002_remove_charitytbl_date', '2024-04-09 04:03:23.770828');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('02rh9qw0s23luhvnqij390jzyjbsrva9', 'e30:1rp3tn:jaSY25pRUHRJAsKCNtf6_h5C952fUNwYKyAG9zmQ3_E', '2024-04-09 10:19:19.352497'),
('clttzuj49iipfj71wggk4pjignrnvmcf', 'eyJ1aWQiOjIsInVuYW1lIjoidXNlcjEifQ:1rplrW:mBbhrj8goJPao_Q8dqvM3kA5DMHeC9s4YNWG3amJTt4', '2024-04-11 09:15:54.936371'),
('pic7rlej63thkgvkr191b5id43xhfbab', 'e30:1rx2bb:Vnwk9LokTl6o3q-YmXGHMN63L-2DRNUDX7GPWM5g2cs', '2024-05-01 10:33:31.778782'),
('tmdizo4bljy5giy85z64mq698azb3qo9', 'e30:1rwzPQ:r3Bu4UtQr3k7R-_m2VV4tDbNHZlnPrGLT-PwHTlMgjk', '2024-05-01 07:08:44.577767'),
('vse8lozyagr0l0sb0ptci1fkdp4u8tjw', 'e30:1rsg1c:L1AZBW53K9xNQyWNpGQ-DdsfOcn6-TvP3Gee_ASY2n8', '2024-04-19 09:38:20.120211'),
('vuid2gvd3uwsg993wdbvmztcj6pf9lxn', 'e30:1ru8H8:fkPqTk3rbhKcx75Wi-9Rfapect0gBkLBv-YlGrq8Isg', '2024-04-23 10:00:22.945156');

-- --------------------------------------------------------

--
-- Table structure for table `foodtruck_assigntbl`
--

CREATE TABLE IF NOT EXISTS `foodtruck_assigntbl` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `food_name` varchar(150) NOT NULL,
  `food_id` varchar(150) NOT NULL,
  `tname` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL,
  `cname` varchar(150) NOT NULL,
  `cid` varchar(150) NOT NULL,
  `fdreq_id` int(3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `foodtruck_assigntbl`
--

INSERT INTO `foodtruck_assigntbl` (`id`, `food_name`, `food_id`, `tname`, `status`, `cname`, `cid`, `fdreq_id`) VALUES
(1, 'Food 1', '19', 'Truck 1', 'rejected', 'charity', '8', 11);

-- --------------------------------------------------------

--
-- Table structure for table `foodtruck_cartitems`
--

CREATE TABLE IF NOT EXISTS `foodtruck_cartitems` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user` varchar(150) NOT NULL,
  `product_id` varchar(150) NOT NULL,
  `quantity` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=30 ;

-- --------------------------------------------------------

--
-- Table structure for table `foodtruck_categorytbl`
--

CREATE TABLE IF NOT EXISTS `foodtruck_categorytbl` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `foodtruck_categorytbl`
--

INSERT INTO `foodtruck_categorytbl` (`id`, `name`) VALUES
(1, 'Testing');

-- --------------------------------------------------------

--
-- Table structure for table `foodtruck_charitytbl`
--

CREATE TABLE IF NOT EXISTS `foodtruck_charitytbl` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cname` varchar(150) NOT NULL,
  `c_license_no` varchar(150) NOT NULL,
  `member` varchar(150) NOT NULL,
  `address` varchar(150) NOT NULL,
  `phone` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `foodtruck_charitytbl`
--

INSERT INTO `foodtruck_charitytbl` (`id`, `cname`, `c_license_no`, `member`, `address`, `phone`, `email`, `password`, `status`) VALUES
(8, 'charity', '324234234', '3', 'Ernakulamm', '9876543210', 'd@gmail.com', '123', 'accepted'),
(9, 'gegeg', 'kdhewfh34', '23', 'Ernakuia,]]', '9809898987', 'a@gamil.com', '123', 'accepted');

-- --------------------------------------------------------

--
-- Table structure for table `foodtruck_complainttbl`
--

CREATE TABLE IF NOT EXISTS `foodtruck_complainttbl` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cname` varchar(150) NOT NULL,
  `msg` varchar(150) NOT NULL,
  `reply` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `foodtruck_complainttbl`
--

INSERT INTO `foodtruck_complainttbl` (`id`, `cname`, `msg`, `reply`) VALUES
(4, 'gegeg', 'shhh', 'accepted');

-- --------------------------------------------------------

--
-- Table structure for table `foodtruck_delivertbl`
--

CREATE TABLE IF NOT EXISTS `foodtruck_delivertbl` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `food_name` varchar(150) NOT NULL,
  `food_id` varchar(150) NOT NULL,
  `tname` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL,
  `cname` varchar(150) NOT NULL,
  `cid` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `foodtruck_delivertbl`
--

INSERT INTO `foodtruck_delivertbl` (`id`, `food_name`, `food_id`, `tname`, `status`, `cname`, `cid`) VALUES
(11, 'Food 1', '19', 'Truck 1', 'delivered', 'charity', '8');

-- --------------------------------------------------------

--
-- Table structure for table `foodtruck_feedbacktbl`
--

CREATE TABLE IF NOT EXISTS `foodtruck_feedbacktbl` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cname` varchar(150) NOT NULL,
  `feedback` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `foodtruck_feedbacktbl`
--

INSERT INTO `foodtruck_feedbacktbl` (`id`, `cname`, `feedback`) VALUES
(4, 'charity', 'very good');

-- --------------------------------------------------------

--
-- Table structure for table `foodtruck_foodreqtbl`
--

CREATE TABLE IF NOT EXISTS `foodtruck_foodreqtbl` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `uname` varchar(150) NOT NULL,
  `uid` varchar(150) NOT NULL,
  `food_name` varchar(150) NOT NULL,
  `food_id` varchar(150) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(150) NOT NULL,
  `cname` varchar(150) NOT NULL,
  `cid` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `foodtruck_foodreqtbl`
--

INSERT INTO `foodtruck_foodreqtbl` (`id`, `uname`, `uid`, `food_name`, `food_id`, `date`, `status`, `cname`, `cid`) VALUES
(11, 'jerin', '9', 'Food 1', '19', '2024-04-17', 'assigned', 'charity', '8');

-- --------------------------------------------------------

--
-- Table structure for table `foodtruck_foodtbl`
--

CREATE TABLE IF NOT EXISTS `foodtruck_foodtbl` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `uname` varchar(150) NOT NULL,
  `uid` varchar(150) NOT NULL,
  `food_name` varchar(150) NOT NULL,
  `category` varchar(150) NOT NULL,
  `district` varchar(150) NOT NULL,
  `city` varchar(150) NOT NULL,
  `quantity` varchar(150) NOT NULL,
  `type` varchar(150) NOT NULL,
  `p_date` date NOT NULL,
  `status` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=22 ;

--
-- Dumping data for table `foodtruck_foodtbl`
--

INSERT INTO `foodtruck_foodtbl` (`id`, `uname`, `uid`, `food_name`, `category`, `district`, `city`, `quantity`, `type`, `p_date`, `status`) VALUES
(20, 'jerin', '9', 'Food 1', 'Testing', 'Pathanamthitta', 'konni', '10', 'Non Veg', '2024-04-17', 'pending'),
(21, 'jerin', '9', 'Food 1', 'Testing', 'erklm', 'konni', '20', 'Veg', '2024-05-03', 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `foodtruck_products`
--

CREATE TABLE IF NOT EXISTS `foodtruck_products` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `quantity` varchar(150) NOT NULL,
  `price` double NOT NULL,
  `description` varchar(500) NOT NULL,
  `image` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `foodtruck_products`
--

INSERT INTO `foodtruck_products` (`id`, `name`, `quantity`, `price`, `description`, `image`) VALUES
(7, 'Testing', '10', 1000, 'Test', 'IMG-20210326-WA0129.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `foodtruck_purchases`
--

CREATE TABLE IF NOT EXISTS `foodtruck_purchases` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `userr` varchar(150) NOT NULL,
  `product` varchar(150) NOT NULL,
  `total_item` varchar(150) NOT NULL,
  `total_price` varchar(150) NOT NULL,
  `card_name` varchar(150) NOT NULL,
  `card_number` double NOT NULL,
  `cvv` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `foodtruck_purchases`
--

INSERT INTO `foodtruck_purchases` (`id`, `userr`, `product`, `total_item`, `total_price`, `card_name`, `card_number`, `cvv`, `status`) VALUES
(1, '9', 'Testing', '1', '800.0', 'jerin', 5.464665464566645e15, '456', 'Confirmed');

-- --------------------------------------------------------

--
-- Table structure for table `foodtruck_rewardtbl`
--

CREATE TABLE IF NOT EXISTS `foodtruck_rewardtbl` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `uid` varchar(150) NOT NULL,
  `uname` varchar(150) NOT NULL,
  `point` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `foodtruck_rewardtbl`
--

INSERT INTO `foodtruck_rewardtbl` (`id`, `uid`, `uname`, `point`) VALUES
(8, '9', 'jerin', '0');

-- --------------------------------------------------------

--
-- Table structure for table `foodtruck_trucktbl`
--

CREATE TABLE IF NOT EXISTS `foodtruck_trucktbl` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `tname` varchar(150) NOT NULL,
  `no_plate` varchar(150) NOT NULL,
  `license_no` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `foodtruck_trucktbl`
--

INSERT INTO `foodtruck_trucktbl` (`id`, `tname`, `no_plate`, `license_no`, `email`, `password`, `status`) VALUES
(5, 'Truck 1', 'Kl 09 12 1223', 'hkdhed23434', 's@gmail.com', '123', 'available');

-- --------------------------------------------------------

--
-- Table structure for table `foodtruck_userregtbl`
--

CREATE TABLE IF NOT EXISTS `foodtruck_userregtbl` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `address` varchar(150) NOT NULL,
  `phone` varchar(150) NOT NULL,
  `gender` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `foodtruck_userregtbl`
--

INSERT INTO `foodtruck_userregtbl` (`id`, `name`, `email`, `address`, `phone`, `gender`, `password`) VALUES
(9, 'jerin', 'j@gmail.com', 'Ernakulam', '9809898987', 'male', '123');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
