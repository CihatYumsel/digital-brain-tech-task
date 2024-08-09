**Digital Brain Technologies - Görev Özeti**

**Cihat YÜMSEL**

**Task 1: Kafka Kurulumu ve Temel İşlemler**

1.  **Kafka\'nın Docker ile Kurulumu:**

> Kafka ve Zookeeper Docker konteynerleri ile kuruldu.
> docker-compose.yml dosyasındaki yapılandırma kullanılarak Kafka ve
> Zookeeper servisleri başlatıldı.

2.  **Kafka Topic Oluşturma:**

Kafka CLI komutları kullanılarak bir topic oluşturuldu. Komutlar:

-   docker-compose exec kafka kafka-topics.sh \--create \--topic
    shop_data \--bootstrap-server kafka:9092 \--partitions 1
    \--replication-factor 1

> Topic'lerin listelenmesi için:

-   docker-compose exec kafka kafka-topics.sh \--list
    \--bootstrap-server kafka:9092

3.  **Mesaj Gönderme:**

Kafka topic\'ine mesaj gönderme komutu:

-   docker-compose exec kafka kafka-console-producer.sh \--topic
    shop_data \--bootstrap-server kafka:9092

Mesaj terminale girilip Enter tuşuna basılarak gönderildi.

4.  **Mesajları Dinleme:**

> Kafka topic\'inden mesajları dinlemek için:

-   docker-compose exec kafka kafka-console-consumer.sh \--topic
    shop_data \--bootstrap-server kafka:9092 \--from-beginning

**Task 2: Web Scraping ve Veri İşleme**

1.  **Web Scraping:**

> scrape_and_send_to_kafka.py dosyasında, requests ve BeautifulSoup
> kütüphaneleri kullanılarak web scraping işlemi yapıldı.

Web sayfasından ürün bilgileri çekildi ve detaylar alındı.

2.  **Verileri Kafka\'ya Gönderme:**

> scrape_and_send_to_kafka.py dosyasında Kafka Producer kullanılarak
> veriler topic\'e gönderildi.

3.  **Veriyi Dosyaya Yazma:**

> kafka_to_file.py dosyasında Kafka Consumer kullanılarak veri data.json
> dosyasına yazıldı.

4.  **REST API Servisi:**

app.py dosyasında Flask kullanılarak veri sunma servisi oluşturuldu.

**Task 3: Dockerize ve GitHub'a Yükleme**

1.  **Dockerize:**

> Proje, Dockerfile\'lar kullanılarak Docker konteynerlarına
> dönüştürüldü. docker-compose.yml dosyası ile servisler oluşturuldu.
>
> **Dockerfile içeriği:**

-   **Dockerfile.app:** Flask uygulaması için.

-   **Dockerfile.producer:** Kafka\'ya veri gönderen producer için.

-   **Dockerfile.consumer:** Kafka\'dan veri tüketen consumer için.

2.  **GitHub'a Yükleme:**

> GitHub\'da bir repo oluşturuldu.
>
> Yerel projeyi GitHub'a yüklemek için:

-   git init

-   git add .

-   git commit -m \"Initial commit\"

-   git remote add origin
    https://github.com/CihatYumsel/digital-brain-tech-task.git

-   git push -u origin master
