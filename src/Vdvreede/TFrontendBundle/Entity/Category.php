<?php

namespace Vdvreede\TFrontendBundle\Entity;

use Doctrine\ORM\Mapping as ORM;
use Gedmo\Mapping\Annotation as Gedmo;

/**
 * Vdv\AccountBundle\Entity\Category
 *
 * @ORM\Table(name="category")
 * @ORM\Entity(repositoryClass="Vdvreede\TFrontendBundle\Repository\CategoryRepository")
 * @Gedmo\Loggable
 */
class Category
{
    
    public static $INCOME = 0;
    public static $EXPENSE = 1;
    
    
    /**
     * @var integer $id
     *
     * @ORM\Column(name="id", type="integer", nullable=false)
     * @ORM\Id
     * @ORM\GeneratedValue(strategy="AUTO")
     */
    private $id;

    /**
     * @var integer $userId
     *
     * @ORM\Column(name="user_id", type="integer", nullable=false)
     */
    private $userId;

    /**
     * @var string $name
     *
     * @ORM\Column(name="name", type="string", length=45, nullable=false)
     */
    private $name;

    /**
     * @var text $description
     *
     * @ORM\Column(name="description", type="text", nullable=true)
     */
    private $description;

    /**
     * @var string $colour
     *
     * @ORM\Column(name="colour", type="string", length=45, nullable=true)
     */
    private $colour;

    /**
     * @var integer $type
     *
     * @ORM\Column(name="type", type="integer", nullable=false)
     */
    private $type;

    /**
     * @var boolean $reportable
     *
     * @ORM\Column(name="reportable", type="boolean", nullable=false)
     */
    private $reportable;

    /**
     * @var User
     *
     * @ORM\ManyToOne(targetEntity="User")
     * @ORM\JoinColumns({
     *   @ORM\JoinColumn(name="user_id", referencedColumnName="id")
     * })
     */
    private $user;
    
     /**
     * @var datetime $created
     * 
     * @ORM\Column(type="datetime")
     * @Gedmo\Timestampable(on="create")
     */
    private $created;
     
    /**
     * @var datetime $updated
     *
     * @ORM\Column(type="datetime", nullable=true)
     * @Gedmo\Timestampable(on="update")
     */
    private $updated;

     /**
     * Returns the category name.
     * 
     * @return string
     */
    public function __toString() {
        return $this->name;
    }

    /**
     * Get id
     *
     * @return integer $id
     */
    public function getId()
    {
        return $this->id;
    }

    /**
     * Set userId
     *
     * @param integer $userId
     */
    public function setUserId($userId)
    {
        $this->userId = $userId;
    }

    /**
     * Get userId
     *
     * @return integer $userId
     */
    public function getUserId()
    {
        return $this->userId;
    }

    /**
     * Set name
     *
     * @param string $name
     */
    public function setName($name)
    {
        $this->name = $name;
    }

    /**
     * Get name
     *
     * @return string $name
     */
    public function getName()
    {
        return $this->name;
    }

    /**
     * Set description
     *
     * @param text $description
     */
    public function setDescription($description)
    {
        $this->description = $description;
    }

    /**
     * Get description
     *
     * @return text $description
     */
    public function getDescription()
    {
        return $this->description;
    }

    /**
     * Set colour
     *
     * @param string $colour
     */
    public function setColour($colour)
    {
        $this->colour = $colour;
    }

    /**
     * Get colour
     *
     * @return string $colour
     */
    public function getColour()
    {
        return $this->colour;
    }

    /**
     * Set type
     *
     * @param integer $type
     */
    public function setType($type)
    {
        $this->type = $type;
    }

    /**
     * Get type
     *
     * @return string $type
     */
    public function getType()
    {
        switch($this->type) {
            case self::$INCOME:
                return 'Income';
                break;
            case self::$EXPENSE:
                return 'Expense';
                break;
        }
    }

    /**
     * Set reportable
     *
     * @param boolean $reportable
     */
    public function setReportable($reportable)
    {
        $this->reportable = $reportable;
    }

    /**
     * Get reportable
     *
     * @return boolean $reportable
     */
    public function getReportable()
    {
        return $this->reportable;
    }

    /**
     * Set user
     *
     * @param Vdvreede\TFrontendBundle\Entity\User $user
     */
    public function setUser(\Vdvreede\TFrontendBundle\Entity\User $user)
    {
        $this->user = $user;
    }

    /**
     * Get user
     *
     * @return Vdvreede\TFrontendBundle\Entity\User $user
     */
    public function getUser()
    {
        return $this->user;
    }
}