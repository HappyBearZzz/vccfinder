-- MySQL dump 10.13  Distrib 5.5.46, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: vccfinder
-- ------------------------------------------------------
-- Server version	5.5.46-0ubuntu0.14.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `commit_cluster`
--

DROP TABLE IF EXISTS `commit_cluster`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commit_cluster` (
  `id` bigint(10) NOT NULL AUTO_INCREMENT,
  `original_id` bigint(10) DEFAULT NULL,
  `repository_id` bigint(10) DEFAULT NULL,
  `sha` varchar(255) DEFAULT NULL,
  `message` text,
  `message_stem` text,
  `cluster` bigint(10) DEFAULT NULL,
  `is_bug_fixed` varchar(45) DEFAULT NULL,
  `author_email` text,
  `committer_email` text,
  `additions` bigint(10) DEFAULT NULL,
  `deletions` bigint(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `commit_cluster_minibatch`
--

DROP TABLE IF EXISTS `commit_cluster_minibatch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commit_cluster_minibatch` (
  `id` bigint(10) NOT NULL AUTO_INCREMENT,
  `original_id` bigint(10) DEFAULT NULL,
  `repository_id` bigint(10) DEFAULT NULL,
  `sha` varchar(255) DEFAULT NULL,
  `message` text,
  `cluster` bigint(10) DEFAULT NULL,
  `is_bug_fixed` varchar(45) DEFAULT NULL,
  `author_email` varchar(255) DEFAULT NULL,
  `committer_email` varchar(255) DEFAULT NULL,
  `additions` bigint(10) DEFAULT NULL,
  `deletions` bigint(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `commits`
--

DROP TABLE IF EXISTS `commits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commits` (
  `id` bigint(20) DEFAULT NULL,
  `repository_id` bigint(20) DEFAULT NULL,
  `is_bug_fixed` text,
  `sha` varchar(255) DEFAULT NULL,
  `url` text,
  `author_email` text,
  `author_name` text,
  `author_when` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `committer_email` text,
  `committer_name` text,
  `committer_when` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `additions` bigint(20) DEFAULT NULL,
  `deletions` bigint(20) DEFAULT NULL,
  `total_changes` bigint(20) DEFAULT NULL,
  `message` text,
  `patch` text,
  `cve` text,
  `files_changed` text,
  KEY `index_id` (`id`),
  KEY `index_repos_sha` (`repository_id`,`sha`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `commits_words`
--

DROP TABLE IF EXISTS `commits_words`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commits_words` (
  `id` bigint(20) DEFAULT NULL,
  `repository_id` bigint(20) DEFAULT NULL,
  `is_bug_fixed` text,
  `sha` varchar(255) DEFAULT NULL,
  `url` text,
  `author_email` text,
  `author_name` text,
  `author_when` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `committer_email` text,
  `committer_name` text,
  `committer_when` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `additions` bigint(20) DEFAULT NULL,
  `deletions` bigint(20) DEFAULT NULL,
  `total_changes` bigint(20) DEFAULT NULL,
  `message` text,
  `patch` text,
  `cve` text,
  `files_changed` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cves`
--

DROP TABLE IF EXISTS `cves`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cves` (
  `id` text,
  `type` text,
  `published` date DEFAULT NULL,
  `updated` date DEFAULT NULL,
  `score` double DEFAULT NULL,
  `gained_access_level` text,
  `access` text,
  `complexity` text,
  `authentication` text,
  `conf` text,
  `integ` text,
  `avail` text,
  `description` text,
  `vendor` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `repositories`
--

DROP TABLE IF EXISTS `repositories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `repositories` (
  `id` int(11) DEFAULT NULL,
  `name` text,
  `description` text,
  `pushed_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `forks_count` int(11) DEFAULT NULL,
  `stargazers_count` int(11) DEFAULT NULL,
  `watchers_count` int(11) DEFAULT NULL,
  `subscribers_count` int(11) DEFAULT NULL,
  `open_issues_count` int(11) DEFAULT NULL,
  `pull_request_count` int(11) DEFAULT NULL,
  `size` int(11) DEFAULT NULL,
  `language` text,
  `default_branch` text,
  `git_url` text,
  `distinct_authors_count` int(11) DEFAULT NULL,
  `commits_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-02-03  9:10:22
